---
id: learning.zephyr-docs.networking.page-66
title: CoAP服务器库
kind: reference
status: maintained
domains: [zephyr, networking, development]
source_url: https://docs.zephyrproject.org/latest/services/connectivity/networking/api/coap_server.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第66章\_CoAP服务器库

原文：[官方页面](https://docs.zephyrproject.org/latest/services/connectivity/networking/api/coap_server.html)。读取日期：2026-10-14；保存的 latest 页面及 HTML 摘要见[来源记录](../SOURCES.md)。

## 66.1 概览（Overview）

Zephyr 自带 CoAP 服务器（CoAP Server），通过服务（Service）监听请求。服务管理套接字通信，再将请求交给已注册的 CoAP 资源（Resource）。

## 66.2 配置服务（Setup）

先在应用的 `prj.conf` 中启用 [`CONFIG_COAP_SERVER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_COAP_SERVER)：

```kconfig
CONFIG_COAP_SERVER=y
```

所有服务进入预定义链接段（Linker Section），每个服务的资源也进入各自链接段。若服务名为 `my_service`，资源段名称需加上 `coap_resource_` 前缀。在应用中创建链接文件 `sections-ram.ld`：

```ld
#include <zephyr/linker/iterable_sections.h>

ITERABLE_SECTION_RAM(coap_resource_my_service, Z_LINK_ITERABLE_SUBALIGN)
```

再在应用 `CMakeLists.txt` 中加入该文件及对应的 CMake 链接器生成器配置：

```cmake
# Support LD linker template
zephyr_linker_sources(DATA_SECTIONS sections-ram.ld)

# Support CMake linker generator
zephyr_iterable_section(NAME coap_resource_my_service
                        GROUP DATA_REGION ${XIP_ALIGN_WITH_INPUT})
```

然后在应用源码中定义服务：

```c
#include <zephyr/net/coap_service.h>

static const uint16_t my_service_port = 5683;

COAP_SERVICE_DEFINE(my_service, "0.0.0.0", &my_service_port, COAP_SERVICE_AUTOSTART);
```

使用 `COAP_SERVICE_AUTOSTART` 标志的服务随 CoAP 服务器线程启动。也可以通过 `coap_service_start`、`coap_service_stop` 手动启动和停止。

> 源码核对译注：当前 [`coap_service.h`](https://github.com/zephyrproject-rtos/zephyr/blob/main/include/zephyr/net/coap_service.h) 将端口参数定义为输入／输出指针；端口设为 0 时，[服务器实现](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/coap/coap_server.c)会回填实际端口。原例固定为 5683，但若改成动态端口，不应保留 `const uint16_t`，应提供可写的 `uint16_t` 存储。

## 66.3 注册资源（Sample Usage）

下面把一个资源注册到前面的服务。GET 处理函数组织并发送响应，PUT 处理函数以返回响应码的方式让服务器代发回复：

```c
#include <zephyr/net/coap_service.h>

static int my_get(struct coap_resource *resource, struct coap_packet *request,
                  struct net_sockaddr *addr, socklen_t addr_len)
{
    static const char *msg = "Hello, world!";
    uint8_t data[CONFIG_COAP_SERVER_MESSAGE_SIZE];
    struct coap_packet response;
    uint16_t id;
    uint8_t token[COAP_TOKEN_MAX_LEN];
    uint8_t tkl, type;

    type = coap_header_get_type(request);
    id = coap_header_get_id(request);
    tkl = coap_header_get_token(request, token);

    /* Determine response type */
    type = (type == COAP_TYPE_CON) ? COAP_TYPE_ACK : COAP_TYPE_NON_CON;

    coap_packet_init(&response, data, sizeof(data), COAP_VERSION_1, type, tkl, token,
                     COAP_RESPONSE_CODE_CONTENT, id);

    /* Set content format */
    coap_append_option_int(&response, COAP_OPTION_CONTENT_FORMAT,
                           COAP_CONTENT_FORMAT_TEXT_PLAIN);

    /* Append payload */
    coap_packet_append_payload_marker(&response);
    coap_packet_append_payload(&response, (uint8_t *)msg, strlen(msg));

    /* Send to response back to the client */
    return coap_resource_send(resource, &response, addr, addr_len, NULL);
}

static int my_put(struct coap_resource *resource, struct coap_packet *request,
                  struct net_sockaddr *addr, socklen_t addr_len)
{
    /* ... Handle the incoming request ... */

    /* Return a CoAP response code as a shortcut for an empty ACK message */
    return COAP_RESPONSE_CODE_CHANGED;
}

static const char * const my_resource_path[] = { "test", NULL };
COAP_RESOURCE_DEFINE(my_resource, my_service, {
    .path = my_resource_path,
    .get = my_get,
    .put = my_put,
});
```

原文称资源处理函数可以返回响应码，让服务器发送空 ACK 响应。

> 译注：这里的“空”指没有负载，不是 CoAP 码为 `0.00` 的 Empty 消息。当前服务器依据原请求类型选择回复类型：确认消息（Confirmable，CON）得到 ACK，非确认消息（Non-confirmable，NON）得到 NON。上面的代码仍是说明示例；报文组装各步骤的返回值应在实际程序中处理。

## 66.4 可观察资源（Observable Resources）

服务器提供观察请求（Observe Request）的解析逻辑，并在服务运行时数据中保存观察者（Observer）。下面用温度传感器演示初始响应及后续通知：

```c
#include <zephyr/kernel.h>
#include <zephyr/drivers/sensor.h>
#include <zephyr/net/coap_service.h>

static void notify_observers(struct k_work *work);
K_WORK_DELAYABLE_DEFINE(temp_work, notify_observers);

static int send_temperature(struct coap_resource *resource,
                            const struct net_sockaddr *addr, socklen_t addr_len,
                            uint16_t age, uint16_t id, const uint8_t *token, uint8_t tkl,
                            bool is_response)
{
    const struct device *dev = DEVICE_DT_GET(DT_ALIAS(ambient_temp0));
    uint8_t data[CONFIG_COAP_SERVER_MESSAGE_SIZE];
    struct coap_packet response;
    char payload[14];
    struct sensor_value value;
    double temp;
    uint8_t type;

    /* Determine response type */
    type = is_response ? COAP_TYPE_ACK : COAP_TYPE_CON;

    if (!is_response) {
        id = coap_next_id();
    }

    coap_packet_init(&response, data, sizeof(data), COAP_VERSION_1, type, tkl, token,
                     COAP_RESPONSE_CODE_CONTENT, id);

    if (age >= 2U) {
        coap_append_option_int(&response, COAP_OPTION_OBSERVE, age);
    }

    /* Set content format */
    coap_append_option_int(&response, COAP_OPTION_CONTENT_FORMAT,
                           COAP_CONTENT_FORMAT_TEXT_PLAIN);

    /* Get the sensor data */
    sensor_sample_fetch_chan(dev, SENSOR_CHAN_AMBIENT_TEMP);
    sensor_channel_get(dev, SENSOR_CHAN_AMBIENT_TEMP, &value);
    temp = sensor_value_to_double(&value);

    snprintk(payload, sizeof(payload), "%0.2f°C", temp);

    /* Append payload */
    coap_packet_append_payload_marker(&response);
    coap_packet_append_payload(&response, (uint8_t *)payload, strlen(payload));

    return coap_resource_send(resource, &response, addr, addr_len, NULL);
}

static int temp_get(struct coap_resource *resource, struct coap_packet *request,
                    struct net_sockaddr *addr, socklen_t addr_len)
{
    uint8_t token[COAP_TOKEN_MAX_LEN];
    uint16_t id;
    uint8_t tkl;
    int r;

    /* Let the CoAP server parse the request and add/remove observers if needed */
    r = coap_resource_parse_observe(resource, request, addr);

    id = coap_header_get_id(request);
    tkl = coap_header_get_token(request, token);

    return send_temperature(resource, addr, addr_len, r == 0 ? resource->age : 0,
                            id, token, tkl, true);
}

static void temp_notify(struct coap_resource *resource, struct coap_observer *observer)
{
    send_temperature(resource, net_sad(&observer->addr), sizeof(observer->addr), resource->age,
                     0, observer->token, observer->tkl, false);
}

static const char * const temp_resource_path[] = { "sensors", "temp1", NULL };
COAP_RESOURCE_DEFINE(temp_resource, my_service, {
    .path = temp_resource_path,
    .get = temp_get,
    .notify = temp_notify,
});

static void notify_observers(struct k_work *work)
{
    if (sys_slist_is_empty(&temp_resource.observers)) {
        return;
    }

    coap_resource_notify(&temp_resource);
    k_work_reschedule(&temp_work, K_SECONDS(1));
}
```

> 译注：`K_WORK_DELAYABLE_DEFINE` 只定义可延迟工作项（Delayable Work Item），原片段没有展示第一次调度。应在应用的适当时机启动 `temp_work`；代码在观察者列表为空时直接返回，之后若新增观察者，也需要有重新启动通知工作的路径。这个片段的 `is_response=true` 固定选择 ACK，实际若接受 NON 请求，应按请求类型组织响应；同时检查 `ambient_temp0` 对应设备是否存在、就绪及传感器读取结果。不能把这个片段视为已经覆盖完整设备生命周期的程序。

## 66.5 CoAP 事件（CoAP Events）

启用 [`CONFIG_NET_MGMT_EVENT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_MGMT_EVENT) 后，可以注册观察者加入／移除、服务启动／停止等事件。下面的回调在事件发生时打印信息：

```c
#include <zephyr/sys/printk.h>
#include <zephyr/net/coap_mgmt.h>
#include <zephyr/net/coap_service.h>

#define COAP_EVENTS_SET (NET_EVENT_COAP_OBSERVER_ADDED | NET_EVENT_COAP_OBSERVER_REMOVED | \
                         NET_EVENT_COAP_SERVICE_STARTED | NET_EVENT_COAP_SERVICE_STOPPED)

void coap_event_handler(uint64_t mgmt_event, struct net_if *iface,
                        void *info, size_t info_length, void *user_data)
{
    switch (mgmt_event) {
    case NET_EVENT_COAP_OBSERVER_ADDED:
        printk("CoAP observer added");
        break;
    case NET_EVENT_COAP_OBSERVER_REMOVED:
        printk("CoAP observer removed");
        break;
    case NET_EVENT_COAP_SERVICE_STARTED:
        if (info != NULL && info_length == sizeof(struct net_event_coap_service)) {
            struct net_event_coap_service *net_event = info;

            printk("CoAP service %s started", net_event->service->name);
        } else {
            printk("CoAP service started");
        }
        break;
    case NET_EVENT_COAP_SERVICE_STOPPED:
        if (info != NULL && info_length == sizeof(struct net_event_coap_service)) {
            struct net_event_coap_service *net_event = info;

            printk("CoAP service %s stopped", net_event->service->name);
        } else {
            printk("CoAP service stopped");
        }
        break;
    }
}

NET_MGMT_REGISTER_EVENT_HANDLER(coap_events, COAP_EVENTS_SET, coap_event_handler, NULL);
```

事件处理函数中的服务信息只有在 `info` 非空且尺寸符合 `struct net_event_coap_service` 时才读取。网络管理事件（Network Management Event）通过宏注册。

## 66.6 CoRE 链接格式与参考（CoRE Link Format）

[`CONFIG_COAP_SERVER_WELL_KNOWN_CORE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_COAP_SERVER_WELL_KNOWN_CORE) 使服务器处理 `.well-known/core` 的 GET 请求，让客户端获得指向该服务器其他资源的超媒体链接（Hypermedia Link）列表。

参见[CoAP 服务 API](https://docs.zephyrproject.org/latest/doxygen/html/group__coap__service.html)、[CoAP 管理事件 API](https://docs.zephyrproject.org/latest/doxygen/html/group__coap__mgmt.html)以及[CoAP 服务示例](P072_CoAP服务示例.md#coap-server)。指南与详细参考页分别跟踪；本轮未构建、读取传感器或运行观察通知测试。


<a id="coap-server"></a>
<a id="coap-server-interface"></a>
<a id="contents"></a>
<a id="id4"></a>
<a id="id5"></a>
<a id="id6"></a>
<a id="id7"></a>
<a id="id8"></a>
<a id="id9"></a>
<a id="id10"></a>
<a id="overview"></a>
<a id="setup"></a>
<a id="id1"></a>
<a id="id2"></a>
<a id="id3"></a>
<a id="sample-usage"></a>
<a id="observable-resources"></a>
<a id="coap-events"></a>
<a id="core-link-format"></a>
<a id="api-reference"></a>

<!-- reading-navigation:start -->

**主线阅读**

[上一篇：CoAP客户端库](P065_CoAP客户端库.md) · [本模块主线目录](../reading/networking.md) · [全部主线](../reading/README.md) · [下一篇：CoAP_OSCORE对象安全](P067_CoAP_OSCORE对象安全.md)

<details>
<summary>原册编号导航（含扩展参考）</summary>

[上一章](P065_CoAP客户端库.md) · [返回大纲](大纲.md) · [下一章](P067_CoAP_OSCORE对象安全.md)

</details>

<!-- reading-navigation:end -->
