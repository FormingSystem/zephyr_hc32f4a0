---
id: learning.zephyr-docs.networking.page-73
title: LwM2M协议栈
kind: reference
status: maintained
domains: [zephyr, networking, development]
source_url: https://docs.zephyrproject.org/latest/services/connectivity/networking/api/lwm2m.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第73章\_LwM2M协议栈

原文：[官方页面](https://docs.zephyrproject.org/latest/services/connectivity/networking/api/lwm2m.html)。读取日期：2026-10-14；保存的 latest 页面及 HTML 摘要见[来源记录](../SOURCES.md)。

## 73.1 概览（Overview）

轻量级机器间通信（Lightweight Machine to Machine，LwM2M）是一种面向设备管理、数据上报和设备执行操作的应用层协议。它建立在 CoAP／UDP 之上，由开放移动联盟（Open Mobile Alliance，OMA）制定[标准](https://openmobilealliance.org/release/LightweightM2M/)。通过 CoAP 分组尺寸优化和支持 REST API 的简单无状态流程，它适合资源受限设备。协议入口见[LwM2M](https://www.openmobilealliance.org/specifications/lwm2m)。

LwM2M 与基础 CoAP 的一个重要区别是：LwM2M 客户端主动连接服务器，随后服务器使用 REST API 管理客户端的各类接口。协议采用简单的资源模型（Resource Model），核心对象（Object）和资源（Resource）在规范中定义。

Zephyr 中通过 [`CONFIG_LWM2M`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LWM2M) 启用该库。

## 73.2 对象和资源示例：设备（Device）

设备对象的定义如下：

| 对象 ID | 名称 | 实例 | 必选性 |
| --- | --- | --- | --- |
| 3 | 设备（Device） | 单实例（Single） | 必需（Mandatory） |

资源操作标记：`R` 为读（Read），`W` 为写（Write），`E` 为执行（Execute）；原文记作 `* R=Read, W=Write, E=Execute`。

| ID | 名称 | 操作 | 实例 | 必选性 | 类型 |
| --- | --- | --- | --- | --- | --- |
| 0 | 制造商（Manufacturer） | R | 单 | 可选 | 字符串（String） |
| 1 | 型号（Model） | R | 单 | 可选 | 字符串 |
| 2 | 序列号（Serial number） | R | 单 | 可选 | 字符串 |
| 3 | 固件版本（Firmware version） | R | 单 | 可选 | 字符串 |
| 4 | 重启（Reboot） | E | 单 | 必需 | — |
| 5 | 恢复出厂设置（Factory Reset） | E | 单 | 可选 | — |
| 6 | 可用电源（Available Power Sources） | R | 多 | 可选 | 整数（Integer），0–7 |
| 7 | 电源电压（Power Source Voltage，mV） | R | 多 | 可选 | 整数 |
| 8 | 电源电流（Power Source Current，mA） | R | 多 | 可选 | 整数 |
| 9 | 电池电量（Battery Level，%） | R | 单 | 可选 | 整数 |
| 10 | 可用内存（Memory Free，原文单位 Kb） | R | 单 | 可选 | 整数 |
| 11 | 错误码（Error Code） | R | 多 | 可选 | 整数，0–8 |
| 12 | 重置错误（Reset Error） | E | 单 | 可选 | — |
| 13 | 当前时间（Current Time） | RW | 单 | 可选 | 时间（Time） |
| 14 | UTC 偏移（UTC Offset） | RW | 单 | 可选 | 字符串 |
| 15 | 时区（Timezone） | RW | 单 | 可选 | 字符串 |
| 16 | 支持的绑定（Supported Binding） | R | 单 | 必需 | 字符串 |
| 17 | 设备类型（Device Type） | R | 单 | 可选 | 字符串 |
| 18 | 硬件版本（Hardware Version） | R | 单 | 可选 | 字符串 |
| 19 | 软件版本（Software Version） | R | 单 | 可选 | 字符串 |
| 20 | 电池状态（Battery Status） | R | 单 | 可选 | 整数，0–6 |
| 21 | 内存总量（Memory Total，原文单位 Kb） | R | 单 | 可选 | 整数 |
| 22 | 扩展设备信息（ExtDevInfo） | R | 多 | 可选 | 对象链接（ObjLnk） |

例如，服务器发送 `READ 3/0/0`，即可读取设备对象默认且唯一的实例 0 中的制造商资源。所有已注册对象和资源 ID 见[OMA LwM2M 注册表](https://www.openmobilealliance.org/specifications/registries)。

Zephyr 库位于[subsys/net/lib/lwm2m](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/lwm2m)，示例位于[samples/net/lwm2m_client](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/net/lwm2m_client)；详细用法见[LwM2M 客户端示例](P074_LwM2M客户端示例.md#lwm2m-client)。示例可以使用普通非安全套接字，也可以使用数据报传输层安全（Datagram Transport Layer Security，DTLS）套接字。

库实现了以下部分：处理网络事件和核心功能的引擎（Engine）；执行引导（BOOTSTRAP）和注册（REGISTRATION）的注册／发现客户端（Registration / Discovery Client，RD Client）；SenML CBOR、SenML JSON、CBOR、TLV、JSON 和纯文本编码；Security、Server、Device、Firmware Update 等规范对象；Light Control、Temperature Sensor、Timer 等扩展 IPSO 智能对象。

其中 SenML 是传感器测量列表（Sensor Measurement Lists），CBOR 是简洁二进制对象表示（Concise Binary Object Representation），TLV 是类型—长度—值（Type-Length-Value），JSON 是 JavaScript 对象表示法（JavaScript Object Notation）。

库默认实现[LwM2M 1.0.2](https://www.openmobilealliance.org/release/LightweightM2M/V1_0_2-20180209-A/OMA-TS-LightweightM2M-V1_0_2-20180209-A.pdf)，可通过 Kconfig 切换为[LwM2M 1.1.1](https://www.openmobilealliance.org/release/LightweightM2M/V1_1_1-20190617-A/)。其他版本见[OMA 版本发布页](https://www.openmobilealliance.org/specifications/lwm2m/releases)。

## 73.3 基本用法（Sample Usage）

先创建 [`lwm2m_ctx`](https://docs.zephyrproject.org/latest/doxygen/html/structlwm2m__ctx.html) 客户端上下文：

```c
/* LwM2M client context */
static struct lwm2m_ctx client;
```

为资源执行操作创建回调。下面的原例在服务器请求重启资源时执行设备重启：

```c
static int device_reboot_cb(uint16_t obj_inst_id, uint8_t *args,
                            uint16_t args_len)
{
        LOG_INF("Device rebooting.");
        LOG_PANIC();
        sys_reboot(0);
        return 0; /* won't reach this */
}
```

RD 客户端可以向应用报告事件。接收事件需提供回调：

```c
static void rd_client_event(struct lwm2m_ctx *client,
                            enum lwm2m_rd_client_event client_event)
{
        switch (client_event) {

        case LWM2M_RD_CLIENT_EVENT_NONE:
                /* do nothing */
                break;

        case LWM2M_RD_CLIENT_EVENT_BOOTSTRAP_REG_FAILURE:
                LOG_DBG("Bootstrap registration failure!");
                break;

        case LWM2M_RD_CLIENT_EVENT_BOOTSTRAP_REG_COMPLETE:
                LOG_DBG("Bootstrap registration complete");
                break;

        case LWM2M_RD_CLIENT_EVENT_BOOTSTRAP_TRANSFER_COMPLETE:
                LOG_DBG("Bootstrap transfer complete");
                break;

        case LWM2M_RD_CLIENT_EVENT_REGISTRATION_FAILURE:
                LOG_DBG("Registration failure!");
                break;

        case LWM2M_RD_CLIENT_EVENT_REGISTRATION_COMPLETE:
                LOG_DBG("Registration complete");
                break;

        case LWM2M_RD_CLIENT_EVENT_REG_TIMEOUT:
                LOG_DBG("Registration timeout!");
                break;

        case LWM2M_RD_CLIENT_EVENT_REG_UPDATE_COMPLETE:
                LOG_DBG("Registration update complete");
                break;

        case LWM2M_RD_CLIENT_EVENT_DEREGISTER_FAILURE:
                LOG_DBG("Deregister failure!");
                break;

        case LWM2M_RD_CLIENT_EVENT_DISCONNECT:
                LOG_DBG("Disconnected");
                break;

        case LWM2M_RD_CLIENT_EVENT_REG_UPDATE:
                LOG_DBG("Registration update");
                break;

        case LWM2M_RD_CLIENT_EVENT_DEREGISTER:
                LOG_DBG("Deregistration client");
                break;

        case LWM2M_RD_CLIENT_EVENT_SERVER_DISABLED:
                LOG_DBG("LwM2M server disabled");
          break;
        }
}
```

然后为安全对象（Security）设置服务器位置与连接方式，并为设备对象（Device）的制造商（Manufacturer）、重启（Reboot）资源设置数据和回调：

```c
/*
 * Server URL of default Security object = 0/0/0
 * Use leshan.eclipse.org server IP (5.39.83.206) for connection
 */
lwm2m_set_string(&LWM2M_OBJ(0, 0, 0), "coap://5.39.83.206");

/*
 * Security Mode of default Security object = 0/0/2
 * 3 = NoSec mode (no security beware!)
 */
lwm2m_set_u8(&LWM2M_OBJ(0, 0, 2), 3);

#define CLIENT_MANUFACTURER "Zephyr Manufacturer"

/*
 * Manufacturer resource of Device object = 3/0/0
 * We use lwm2m_set_res_data() function to set a pointer to the
 * CLIENT_MANUFACTURER string.
 * Note the LWM2M_RES_DATA_FLAG_RO flag which stops the engine from
 * trying to assign a new value to the buffer.
 */
lwm2m_set_res_data(&LWM2M_OBJ(3, 0, 0), CLIENT_MANUFACTURER,
                   sizeof(CLIENT_MANUFACTURER),
                   LWM2M_RES_DATA_FLAG_RO);

/* Reboot resource of Device object = 3/0/4 */
lwm2m_register_exec_callback(&LWM2M_OBJ(3, 0, 4), device_reboot_cb);
```

> 源码核对译注：当前官方 [`lwm2m.h`](https://github.com/zephyrproject-rtos/zephyr/blob/main/include/zephyr/net/lwm2m.h) 使用 `lwm2m_set_res_buf()` 设置资源缓冲区，参数分别包含容量、当前数据长度和标志。原例的 `lwm2m_set_res_data()` 是旧接口名称，可对照当前[客户端源码](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/net/lwm2m_client/src/lwm2m-client.c)中的制造商资源初始化。原例 `5.39.83.206` 为历史服务器地址，不表示读取时仍对应可用服务；`NoSec` 明确不提供通信保护。

最后启动 RD 客户端，由它启动 LwM2M 引擎。[`lwm2m_rd_client_start()`](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#ga9dfd46b8a535b1f28e644dc18f57fd79) 的第二个参数是端点名称（Endpoint Name），在同一服务器上必须唯一：

```c
(void)memset(&client, 0x0, sizeof(client));
lwm2m_rd_client_start(&client, "unique-endpoint-name", 0, rd_client_event);
```

> 源码核对译注：当前头文件的启动函数有第五个参数 `lwm2m_observe_cb_t observe_cb`。没有观察事件回调时可传 `NULL`；原页的四参数调用未随接口更新。原代码保留用于对照，实际应用还需检查初始化及启动返回值。

## 73.4 安全模式（LwM2M Security Modes）

库可以不启用安全，也可以使用 DTLS 保护通信。启用 [`CONFIG_LWM2M_DTLS_SUPPORT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LWM2M_DTLS_SUPPORT) 后，可使用预共享密钥（Pre-Shared Key，PSK）或 X.509 证书。引擎从安全对象 ID 0 读取凭据并送入 TLS 凭据子系统，见[安全套接字文档](P040_BSD套接字.md#secure-sockets-interface)。

| 模式 | 安全对象所需资源 |
| --- | --- |
| PSK | 安全模式（ID 2）设为 `0`；身份（ID 3）保存二进制 PSK ID；秘密密钥（ID 5）保存二进制 PSK。十六进制文本须先转为二进制再存储 |
| X509 | 安全模式（ID 2）设为 `2`；身份（ID 3）保存客户端证书；秘密密钥（ID 5）保存对应私钥；服务器公钥（ID 4）保存服务器证书或签署证书链的 CA 证书 |
| NoSec | 安全模式（ID 2）设为 `3`，不使用安全保护 |

启用 [`CONFIG_MBEDTLS_PEM_PARSE_C`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MBEDTLS_PEM_PARSE_C)／[`CONFIG_MBEDTLS_PEM_WRITE_C`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MBEDTLS_PEM_WRITE_C) 时，可以输入 PEM 格式证书和私钥，否则须用二进制 DER 格式。PEM 是隐私增强邮件（Privacy-Enhanced Mail）文本格式，DER 是可辨别编码规则（Distinguished Encoding Rules）。

所有模式的服务器 URI 资源（ID 0）都必须包含完整目标 URI。使用域名时，还需启用 DNS 解析器（DNS Resolver）。

原文推荐以下选项减少重新连接时的 DTLS 握手流量：

- [`CONFIG_LWM2M_DTLS_CID`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LWM2M_DTLS_CID)：启用 DTLS 连接标识（Connection Identifier）。服务器支持并保留相应会话时，设备长时间空闲后恢复可免去重新握手，对 NAT 映射超时尤其有帮助。
- [`CONFIG_LWM2M_TLS_SESSION_CACHING`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LWM2M_TLS_SESSION_CACHING)：在回退到完整握手前尝试会话缓存（Session Cache）。服务器仍缓存会话时，可以减少握手报文；原文强调其主要效果是避免完整注册。

[`lwm2m_ctx`](https://docs.zephyrproject.org/latest/doxygen/html/structlwm2m__ctx.html) 中的凭据加载和套接字配置回调可以保持 `NULL`，使用默认实现。使用外部 TLS 栈或非默认套接字选项时，可覆盖 `lwm2m_ctx.load_credentials()` 或 `lwm2m_ctx.set_socketoptions()`。

PSK 模式安全对象示例：

```c
/* "000102030405060708090a0b0c0d0e0f" */
static unsigned char client_psk[] = {
        0x00, 0x01, 0x02, 0x03, 0x04, 0x05, 0x06, 0x07,
        0x08, 0x09, 0x0a, 0x0b, 0x0c, 0x0d, 0x0e, 0x0f
};

static const char client_identity[] = "Client_identity";

lwm2m_set_string(&LWM2M_OBJ(LWM2M_OBJECT_SECURITY_ID, 0, 0), "coaps://lwm2m.example.com");
lwm2m_set_u8(&LWM2M_OBJ(LWM2M_OBJECT_SECURITY_ID, 0, 2), LWM2M_SECURITY_PSK);
/* Set the client identity as a string, but this could be binary as well */
lwm2m_set_string(&LWM2M_OBJ(LWM2M_OBJECT_SECURITY_ID, 0, 3), client_identity);
/* Set the client pre-shared key (PSK) */
lwm2m_set_opaque(&LWM2M_OBJ(LWM2M_OBJECT_SECURITY_ID, 0, 5), client_psk, sizeof(client_psk));
```

X509 证书模式示例：

```c
static const char certificate[] = "-----BEGIN CERTIFICATE-----\nMIIB6jCCAY+gAw...";
static const char key[] = "-----BEGIN EC PRIVATE KEY-----\nMHcCAQ...";
static const char root_ca[] = "-----BEGIN CERTIFICATE-----\nMIIBaz...";

lwm2m_set_string(&LWM2M_OBJ(LWM2M_OBJECT_SECURITY_ID, 0, 0), "coaps://lwm2m.example.com");
lwm2m_set_u8(&LWM2M_OBJ(LWM2M_OBJECT_SECURITY_ID, 0, 2), LWM2M_SECURITY_CERT);
lwm2m_set_string(&LWM2M_OBJ(LWM2M_OBJECT_SECURITY_ID, 0, 3), certificate);
lwm2m_set_string(&LWM2M_OBJ(LWM2M_OBJECT_SECURITY_ID, 0, 5), key);
lwm2m_set_string(&LWM2M_OBJ(LWM2M_OBJECT_SECURITY_ID, 0, 4), root_ca);
```

这些密钥字节与省略的证书文本为官方示例材料，不能把省略号内容当作完整证书。

调用 [`lwm2m_rd_client_start()`](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#ga9dfd46b8a535b1f28e644dc18f57fd79) 前，设置用于保存 DTLS 凭据的安全标签 `tls_tag`。原文说明一般可用 1：

```c
(void)memset(&client, 0x0, sizeof(client));
client.tls_tag = 1; /* <---- */
lwm2m_rd_client_start(&client, "endpoint-name", 0, rd_client_event);
```

这里的启动调用同样需要按当前接口补充第五个参数。完整示例见[LwM2M 客户端](P074_LwM2M客户端示例.md#lwm2m-client)。

## 73.5 多线程使用（Multi-thread Usage）

可以通过 `lwm2m_set_u8` 等接口写入资源。当一次需要修改多个资源时，使用 `lwm2m_registry_lock` 锁住注册表，完成整组写入后再解锁：

```c
lwm2m_registry_lock();
lwm2m_set_u32(&LWM2M_OBJ(1, 0, 1), 60);
lwm2m_set_u8(&LWM2M_OBJ(5, 0, 3), 0);
lwm2m_set_f64(&LWM2M_OBJ(3303, 0, 5700), value);
lwm2m_registry_unlock();
```

这对复合观察（Composite Observation）尤其有用：引擎在整组操作完成后再更新并发送通知，通常可以减少消息数量。这里的锁用于协调注册表访问，不等同于暂停整个系统的所有线程。

## 73.6 时间序列数据（Time Series Data）

LwM2M 1.1 引入 SenML CBOR 和 SenML JSON，支持在 READ、NOTIFY、SEND 中发送时间序列。资源启用数据缓存（Data Cache）后，每次写入形成带时间戳的记录，随后作为该资源读、通知或发送操作的内容返回。

仅固定尺寸资源支持缓存，类型包括有符号／无符号 8–64 位整数、浮点数（Float）和布尔值（Boolean）。

### 启用和配置（Enabling and Configuring）

启用 [`CONFIG_LWM2M_RESOURCE_DATA_CACHE_SUPPORT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LWM2M_RESOURCE_DATA_CACHE_SUPPORT)，为每个资源独立分配 [`lwm2m_time_series_elem`](https://docs.zephyrproject.org/latest/doxygen/html/structlwm2m__time__series__elem.html) 数组，并调用 [`lwm2m_enable_cache()`](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#ga6975c5c4825afaccc52741eb54aca4cb)：

```c
/* Allocate data cache storage */
static struct lwm2m_time_series_elem temperature_cache[10];
/* Enable data cache */
lwm2m_enable_cache(LWM2M_OBJ(IPSO_OBJECT_TEMP_SENSOR_ID, 0, SENSOR_VALUE_RID),
        temperature_cache, ARRAY_SIZE(temperature_cache));
```

> 源码核对译注：当前函数接收 `const struct lwm2m_obj_path *`，而 `LWM2M_OBJ(...)` 生成结构体值，见官方 [`lwm2m_path.h`](https://github.com/zephyrproject-rtos/zephyr/blob/main/include/zephyr/net/lwm2m_path.h)。原例首参缺少取地址符，当前接口应使用 `&LWM2M_OBJ(...)`。

[`lwm2m_cache_free_slots_get()`](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#ga00d29a0c4935fc255e74b8c22ac49de1) 返回还能存放多少个采样；查询失败返回负 `errno`。引擎默认允许 4 个资源启用缓存，可通过 [`CONFIG_LWM2M_MAX_CACHED_RESOURCES`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LWM2M_MAX_CACHED_RESOURCES) 增加，代价是增加静态内存占用。

缓存依赖 [`CONFIG_LWM2M_RW_SENML_CBOR_SUPPORT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LWM2M_RW_SENML_CBOR_SUPPORT) 或 [`CONFIG_LWM2M_RW_SENML_JSON_SUPPORT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LWM2M_RW_SENML_JSON_SUPPORT)。原文还要求 [`CONFIG_POSIX_TIMERS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_POSIX_TIMERS)，以便取得系统时间戳。

> 源码核对译注：当前库 [Kconfig](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/lwm2m/Kconfig) 的缓存依赖项列出 SenML 格式，并说明需要 `time()` 提供当前 Unix 时间戳；[注册表实现](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/lwm2m/lwm2m_registry.c) 在 `time(NULL)<=0` 时放弃缓存本次采样。因此不能只开启格式选项而忽略系统时间是否有效。

### 读写操作（Read and Write Operations）

READ、SEND 或 NOTIFY 内部读取资源时，将缓存全部内容编码到负载。启用缓存会使该资源已注册的读回调被忽略。调用 `lwm2m_set_*` 时写入缓存；可通过 [`lwm2m_set_cache_filter()`](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#gac4e7da0353914601c3ec101415c2e110) 注册缓存过滤回调，按应用规则丢弃原本有效的采样。

### 限制（Limitations）

应手动控制缓存大小，使内容适合通常的分组尺寸。原文称“缓存满时，新值被丢弃”。

> 源码核对译注：当前 Kconfig 已提供两种满缓存策略，默认 [`CONFIG_LWM2M_CACHE_DROP_OLDEST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LWM2M_CACHE_DROP_OLDEST) 丢弃最旧记录后接纳新值；只有选择 [`CONFIG_LWM2M_CACHE_DROP_LATEST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LWM2M_CACHE_DROP_LATEST) 才丢弃新值。当前 `lwm2m_cache_write()` 也按该选项分支，不能把原页描述当成当前唯一行为。

## 73.7 SEND 调度辅助对象（Send Scheduler Helper Objects）

可选 SEND 调度器在缓存资源之上提供调度控制对象 `10523` 和采样规则对象 `10524`，决定哪些采样保留、何时触发 LwM2M SEND。

### 启用和接入（Enabling and Wiring）

1. 启用 [`CONFIG_LWM2M_SEND_SCHEDULER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LWM2M_SEND_SCHEDULER)，需要 LwM2M 1.1 SEND 支持及 [`CONFIG_LWM2M_RESOURCE_DATA_CACHE_SUPPORT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LWM2M_RESOURCE_DATA_CACHE_SUPPORT)。
2. 调度对象会自动注册；启动 RD 客户端之前，先配置资源缓存。
3. 对每个由调度器管理的缓存资源，用 [`lwm2m_set_cache_filter()`](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#gac4e7da0353914601c3ec101415c2e110) 安装 [`lwm2m_send_sched_cache_filter()`](https://docs.zephyrproject.org/latest/doxygen/html/lwm2m__send__scheduler_8h.html#acc3495441c7fb3391211a360d0602431)。
4. 在 RD 回调收到 `LWM2M_RD_CLIENT_EVENT_REGISTRATION_COMPLETE` 或 `LWM2M_RD_CLIENT_EVENT_REG_UPDATE_COMPLETE` 时调用 [`lwm2m_send_sched_handle_registration_event()`](https://docs.zephyrproject.org/latest/doxygen/html/lwm2m__send__scheduler_8h.html#a896f3773c77143e90858bdeab8ba326a)，使缓存采样紧随注册交换发送。

### 调度控制对象（Scheduler Control，10523）

这是单实例对象，控制全局行为：

| 资源 | 作用 |
| --- | --- |
| `0: paused` | 暂停接纳新的缓存采样 |
| `1: max-samples` | 所有资源缓存采样总数上限；达到时强制 SEND，`0` 禁用此限制 |
| `2: max-age` | 最旧采样的最大年龄，单位秒；达到时触发 SEND，`0` 禁用 |
| `3: flush` | 执行资源，立即对所有已配置规则路径触发 SEND |
| `4: flush-on-update` | 默认启用；注册或注册更新成功时，触发缓存资源 SEND |

### 采样规则对象（Sampling Rules，10524）

每个实例描述一个受监视的缓存资源。`/10524/X/0` 保存资源路径，`/10524/X/1` 最多包含 4 条规则字符串：

| 属性 | 触发条件 |
| --- | --- |
| `gt=<float>` | 采样向上跨越阈值 |
| `lt=<float>` | 采样向下跨越阈值 |
| `st=<float>` | 与上次已上报值的绝对差大于或等于阈值 |
| `pmin=<int>` | 两个被接纳采样之间的最小秒数 |
| `pmax=<int>` | 即使数值未变化，也至少每隔 `pmax` 秒强制保留一个采样 |

实例没有配置规则时，接纳所有输入采样。受控资源缓存耗尽，或全局 `max-samples`／`max-age` 达限时，也会强制 SEND。

## 73.8 引擎状态与应用事件（Engine and Application Events）

引擎通过回调向应用报告事件。官方状态机图展示事件产生的位置；表中事件均省略共同前缀 `LWM2M_RD_CLIENT_EVENT_`。

![LwM2M引擎状态机（LwM2M engine state machine），官方SVG原图](images/lwm2m_engine_state_machine.svg)

图中 connecting、connected、recovering、disconnecting、disconnected、stopped 分别表示连接中、已连接、恢复中、断开中、已断开、已停止；IDLE、INIT、SUSPENDED 分别表示空闲、初始化和挂起。原 SVG 保持原始字节，包括其文本与显示兼容信息。

| 原文事件 ID | 事件名 | 含义与触发条件 |
| --- | --- | --- |
| 0 | NONE | 无事件 |
| 1 | BOOTSTRAP_REG_FAILURE | 引导注册超时或失败 |
| 2 | BOOTSTRAP_REG_COMPLETE | 引导注册成功 |
| 3 | BOOTSTRAP_TRANSFER_COMPLETE | 收到服务器的引导完成命令 |
| 4 | REGISTRATION_FAILURE | 服务器拒绝注册尝试 |
| 5 | REGISTRATION_COMPLETE | 收到注册成功响应，或使用会话恢复成功注册 |
| 6 | REG_TIMEOUT | 套接字错误或消息超时导致注册状态丢失，客户端失去服务器连接 |
| 7 | REG_UPDATE_COMPLETE | 收到注册更新成功响应 |
| 8 | DEREGISTER_FAILURE | 注销超时或失败 |
| 9 | DISCONNECT | 客户端已注销并停止；仅在应用请求停止时触发 |
| 10 | QUEUE_MODE_RX_OFF | 仅用于队列模式；配置的接收时段结束，不再主动监听输入分组 |
| 11 | ENGINE_SUSPENDED | 调用 [`lwm2m_engine_pause()`](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#ga1a4dadb822a8241c5bdf339c21cc57a4) 后暂停；状态机及处理线程挂起，计时器停止，不再触发通知 |
| 12 | SERVER_DISABLED | 服务器执行禁用命令；客户端注销并在禁用期间保持空闲 |
| 13 | NETWORK_ERROR | 网络发送多次失败，无法访问服务器或回退到引导，引擎无法自行恢复而停止 |

> 源码核对译注：表和图保留原页编号；当前头文件枚举的 `NETWORK_ERROR` 为 12，`REG_UPDATE` 为 13，`DEREGISTER` 为 14，`SERVER_DISABLED` 为 15。应用应使用符号名称，不要根据原图表硬编码整数。

引擎自动处理大多数状态转换；应用主要处理已停止或无法自行恢复的情况。原文建议如下：

| 事件名 | 应用处理方式及通信状态 |
| --- | --- |
| NONE | 忽略 |
| BOOTSTRAP_REG_FAILURE | 尝试恢复网络，再调用 [`lwm2m_rd_client_start()`](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#ga9dfd46b8a535b1f28e644dc18f57fd79)；也可能是配置问题 |
| BOOTSTRAP_REG_COMPLETE | 无需动作 |
| BOOTSTRAP_TRANSFER_COMPLETE | 无需动作 |
| REGISTRATION_FAILURE | 自动重新注册，无需主动重启；可能需要引导或修正配置，当前不能收发数据 |
| REGISTRATION_COMPLETE | 无需动作，可以收发数据 |
| REG_TIMEOUT | 自动重新注册，当前不能收发数据 |
| REG_UPDATE_COMPLETE | 无需动作，可以收发数据 |
| DEREGISTER_FAILURE | 自动进入空闲，无需动作，不能收发数据 |
| DISCONNECT | 因 [`lwm2m_rd_client_stop()`](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#gafd87e5d975c4d88973ac3e95e4d156ac) 而停止；若需要连接，再调用 [`lwm2m_rd_client_start()`](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#ga9dfd46b8a535b1f28e644dc18f57fd79) |
| QUEUE_MODE_RX_OFF | 无需动作；可以发送，不能接收；任何发送会触发注册更新 |
| ENGINE_SUSPENDED | 用 [`lwm2m_engine_resume()`](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#ga178fea0407a5e98c4f5d5ad69688853a) 恢复；挂起期间不能收发数据 |
| SERVER_DISABLED | 禁用期间不能收发，到期后自动重新注册 |
| NETWORK_ERROR | 尝试恢复网络，再启动客户端；也可能是配置问题 |

这里“发送”指调用 [`lwm2m_send_cb()`](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#ga026cc9288d2de17ec557e08b9b987ebc)，或写入受观察资源以触发 NOTIFY；“接收”指服务器发来的读、写、执行操作，应用可为这些操作注册回调。

## 73.9 注册生存期与活动周期（Lifetime and Activity Period）

三个 Kconfig 选项与一个运行时值决定客户端发送注册更新（LwM2M Update）的频率：

| 变量 | 作用 |
| --- | --- |
| 注册生存期（Registration Lifetime） | 注册在服务器端的有效时长，设备应在到期前发送更新 |
| [`CONFIG_LWM2M_ENGINE_DEFAULT_LIFETIME`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LWM2M_ENGINE_DEFAULT_LIFETIME) | 引导服务器未设置时的默认值，也是客户端接受的最小生存期 |
| [`CONFIG_LWM2M_UPDATE_PERIOD`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LWM2M_UPDATE_PERIOD) | 下次更新前允许保持空闲的时长 |
| [`CONFIG_LWM2M_SECONDS_TO_UPDATE_EARLY`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LWM2M_SECONDS_TO_UPDATE_EARLY) | 生存期到期前发送更新的最小提前量 |

默认方式按提前量计算更新时机：

![默认注册更新时机（Seconds to update early），官方原图](images/lwm2m_lifetime_seconds_early.png)

图中 Registration lifetime 为注册生存期，SECONDS_TO_UPDATE_EARLY 为提前秒数，UPDATE 为更新。服务器修改生存期会改变客户端更新周期；在 IPv4 网络常用的队列模式（Queue Mode）中，也会改变服务器可访问设备的时机。

同时设置更新周期时，采用两个条件中先到期的那个：

![同时设置更新周期与提前量（Update period and early margin），官方原图](images/lwm2m_lifetime_both.png)

图中 UPDATE_PERIOD 为更新周期。这样可以使用较长注册生存期，同时更准确地控制周期，即使服务器改变生存期参数，也仍受指定周期约束。为防止过量发送，运行时更新频率最多为每 15 秒一次。

> 源码核对译注：当前 [`next_update()`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/lwm2m/lwm2m_rd_client.c) 先对“周期”和“生存期减提前量”取较小值，再施加 15 秒下限。`CONFIG_LWM2M_UPDATE_PERIOD=0` 表示由生存期和提前量控制，而不是不断立即更新。

## 73.10 LwM2M Shell

启用 [`CONFIG_LWM2M_SHELL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LWM2M_SHELL) 后，可以通过 Zephyr Shell 测试资源的读、写、执行，以及客户端启动、停止、暂停、恢复。官方说明它用于测试，生产系统不应启用。

一种用途是在服务器端测试需要设备本地动作、又无法远程触发时，通过通用异步收发器（Universal Asynchronous Receiver/Transmitter，UART）执行客户端操作。原始帮助输出如下：

```text
uart:~$ lwm2m
lwm2m - LwM2M commands
Subcommands:
  send    :send PATHS
          LwM2M SEND operation

  exec    :exec PATH [PARAM]
          Execute a resource

  read    :read PATH [OPTIONS]
          Read value from LwM2M resource
          -x   Read value as hex stream (default)
          -s   Read value as string
          -b   Read value as bool (1/0)
          -uX  Read value as uintX_t
          -sX  Read value as intX_t
          -f   Read value as float
          -t   Read value as time_t

  write   :write PATH [OPTIONS] VALUE
          Write into LwM2M resource
          -s   Write value as string (default)
          -b   Write value as bool
          -uX  Write value as uintX_t
          -sX  Write value as intX_t
          -f   Write value as float
          -t   Write value as time_t

  create  :create PATH
          Create object or resource instance

  delete  :delete PATH
          Delete object or resource instance

  cache   :cache PATH NUM
          Enable data cache for resource
          PATH is LwM2M path
          NUM how many elements to cache

  start   :start EP_NAME [BOOTSTRAP FLAG]
          Start the LwM2M RD (Registration / Discovery) Client
          -b   Set the bootstrap flag (default 0)

  stop    :stop [OPTIONS]
          Stop the LwM2M RD (De-register) Client
          -f   Force close the connection

  update  :Trigger Registration Update of the LwM2M RD Client

  pause   :LwM2M engine thread pause
  resume  :LwM2M engine thread resume
  lock    :Lock the LwM2M registry
  unlock  :Unlock the LwM2M registry
  obs     : List observations
  ls      : ls [PATH]
          List objects, instances, resources
```

命令还包括对象／资源实例创建与删除、缓存启用、注册更新、注册表加锁与解锁、观察列表及对象列表。`PATH` 是 LwM2M 对象路径，不是文件系统目录；`uart:~$` 是设备 Shell 提示符。

## 73.11 API 参考（API Reference）

参见[LwM2M 高层 API](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html)及[客户端示例](P074_LwM2M客户端示例.md#lwm2m-client)。指南与详细接口页分别跟踪。本轮未注册远端设备、执行重启／恢复出厂命令、部署密钥、构建或运行协议测试。


<a id="lightweight-m2m-lwm2m"></a>
<a id="lwm2m-interface"></a>
<a id="contents"></a>
<a id="id8"></a>
<a id="id9"></a>
<a id="id10"></a>
<a id="id11"></a>
<a id="id12"></a>
<a id="id13"></a>
<a id="id14"></a>
<a id="id15"></a>
<a id="id16"></a>
<a id="id17"></a>
<a id="id18"></a>
<a id="id19"></a>
<a id="id20"></a>
<a id="id21"></a>
<a id="id22"></a>
<a id="id23"></a>
<a id="id24"></a>
<a id="overview"></a>
<a id="example-lwm2m-object-and-resources-device"></a>
<a id="sample-usage"></a>
<a id="lwm2m-security-modes"></a>
<a id="lwm2m-security"></a>
<a id="multi-thread-usage"></a>
<a id="support-for-time-series-data"></a>
<a id="enabling-and-configuring"></a>
<a id="read-and-write-operations"></a>
<a id="limitations"></a>
<a id="send-scheduler-helper-objects"></a>
<a id="enabling-and-wiring"></a>
<a id="scheduler-control-object-10523"></a>
<a id="sampling-rules-object-10524"></a>
<a id="lwm2m-engine-and-application-events"></a>
<a id="id2"></a>
<a id="id3"></a>
<a id="id4"></a>
<a id="configuring-lifetime-and-activity-period"></a>
<a id="id5"></a>
<a id="id6"></a>
<a id="id7"></a>
<a id="lwm2m-shell"></a>
<a id="id1"></a>
<a id="api-reference"></a>
<a id="lwm2m-api-reference"></a>

<!-- reading-navigation:start -->

**主线阅读**

[上一篇：CoAP_OSCORE对象安全](P067_CoAP_OSCORE对象安全.md) · [本模块主线目录](../reading/networking.md) · [全部主线](../reading/README.md) · [下一篇：FTP客户端库](P075_FTP客户端库.md)

<details>
<summary>原册编号导航（含扩展参考）</summary>

[上一章](P072_CoAP服务示例.md) · [返回大纲](大纲.md) · [下一章](P074_LwM2M客户端示例.md)

</details>

<!-- reading-navigation:end -->
