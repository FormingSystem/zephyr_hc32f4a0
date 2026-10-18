---
id: learning.zephyr-docs.networking.page-32
title: DNS解析
kind: reference
status: maintained
domains: [zephyr, networking, development]
source_url: https://docs.zephyrproject.org/latest/services/connectivity/networking/api/dns_resolve.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第32章\_DNS解析

原文：[官方页面](https://docs.zephyrproject.org/latest/services/connectivity/networking/api/dns_resolve.html)。读取日期：2026-10-14；保存的 latest 页面及 HTML 摘要见[来源记录](../SOURCES.md)。

## 32.1\_概览（Overview）

域名系统（Domain Name System，DNS）解析器依据 [RFC 1035](https://datatracker.ietf.org/doc/html/rfc1035.html) 实现基本名称解析，支持 IPv4／IPv6 地址和规范名称（Canonical Name，CNAME）应答。

收到 CNAME 时，解析器发起新的 DNS 查询；额外查询次数由 [`CONFIG_DNS_RESOLVER_ADDITIONAL_QUERIES`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_DNS_RESOLVER_ADDITIONAL_QUERIES) 控制。

启用 [`CONFIG_MDNS_RESOLVER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MDNS_RESOLVER) 可使用组播 DNS（Multicast DNS，mDNS）客户端解析器，详见 [RFC 6762](https://datatracker.ietf.org/doc/html/rfc6762.html)。启用 [`CONFIG_LLMNR_RESOLVER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LLMNR_RESOLVER) 可使用链路本地组播名称解析（Link-Local Multicast Name Resolution，LLMNR）客户端，详见 [RFC 4795](https://datatracker.ietf.org/doc/html/rfc4795.html)。

配置定义位于 [`subsys/net/lib/dns/Kconfig`](../../../subsys/net/lib/dns/Kconfig)，API 定义位于 [`include/zephyr/net/dns_resolve.h`](../../../include/zephyr/net/dns_resolve.h)。

## 32.2\_基于 DNS 的服务发现（DNS-based Service Discovery）

使用 [`dns_resolve_service()`](https://docs.zephyrproject.org/latest/doxygen/html/group__dns__resolve.html#gaf28f6f8baa97d0b2341e1bdc02b6cb8c) 可执行 [RFC 6763](https://datatracker.ietf.org/doc/html/rfc6763.html) 的服务发现查询。返回的服务描述传给应用提供的回调（Callback）；API 把地址族设为 `AF_LOCAL`，表示值是服务描述，而不是 IPv4 或 IPv6 地址。

原例查询 `_http._tcp.dns-sd.org`：

```c
#include <zephyr/net/dns_resolve.h>

#define MAX_STR_LEN CONFIG_DNS_RESOLVER_MAX_NAME_LEN

static void dns_result_cb(enum dns_resolve_status status,
                          struct dns_addrinfo *info,
                          void *user_data)
{
     if (status == DNS_EAI_CANCELED) {
             /* dns: Timeout while resolving name */
             return;
     }

     if (status == DNS_EAI_INPROGRESS && info) {
             char str[MAX_STR_LEN + 1];

             if (info->ai_family == NET_AF_INET) {
                     net_addr_ntop(NET_AF_INET,
                                   &net_sin(&info->ai_addr)->sin_addr,
                                   str, NET_IPV4_ADDR_LEN);
             } else if (info->ai_family == NET_AF_INET6) {
                     net_addr_ntop(NET_AF_INET6,
                                   &net_sin6(&info->ai_addr)->sin6_addr,
                                   str, NET_IPV6_ADDR_LEN);
             } else if (info->ai_family == AF_LOCAL) {
                     /* service discovery */
                     memset(str, 0, MAX_STR_LEN);
                     memcpy(str, info->ai_canonname,
                            MIN(info->ai_addrlen, MAX_STR_LEN));
             } else {
                     strncpy(str, "Invalid proto family", MAX_STR_LEN + 1);
             }

             str[MAX_STR_LEN] = '\0';

             printk("dns: %s\n", str);
             return;
     }

     if (status == DNS_EAI_ALLDONE) {
             printk("dns: All results received\n");
             return;
     }

     if (status == DNS_EAI_FAIL) {
             printk("dns: No such name found.\n");
             return;
     }

     printk("dns: Unhandled status %d received (errno %d)\n", status, errno);
}

#define DNS_TIMEOUT (MSEC_PER_SEC * 5) /* in ms */

static void discover_service(void)
{
     int ret = dns_resolve_service(dns_resolve_get_default(),
                                   "_http._tcp.dns-sd.org",
                                   NULL, dns_result_cb,
                                   NULL, DNS_TIMEOUT);
     ...
}
```

代码注释译文：`DNS_EAI_CANCELED` 分支表示解析超时；`AF_LOCAL` 分支处理服务发现；`DNS_TIMEOUT` 的单位为毫秒。回调在进行中的结果到达时分别格式化 IPv4、IPv6 或服务描述；全部结果结束、查询失败或其他状态则打印相应消息。

原文紧接着写“以上查询会返回如下输出”，但本次读取的页面未附实际输出内容；此处不另造查询结果。

服务描述可能很长，返回包也可能较大，需按预期数据调整：

- [`CONFIG_DNS_RESOLVER_MAX_ANSWER_SIZE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_DNS_RESOLVER_MAX_ANSWER_SIZE)：可处理应答的最大大小，默认 `512` 字节，原文给出的典型调整值为 `1024`。
- [`CONFIG_DNS_RESOLVER_MAX_NAME_LEN`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_DNS_RESOLVER_MAX_NAME_LEN)：返回名称的最大长度，按预期数据确定，原文举例为 `128` 字节。

> 源码跟踪译注：示例中的省略号表示待补充代码，需检查查询提交的返回值。示例缓冲区为 `MAX_STR_LEN + 1`，而地址格式化调用传入 `NET_IPV4_ADDR_LEN` 或 `NET_IPV6_ADDR_LEN`，调整名称长度时须保证真实缓冲区也容纳相应地址字符串。本轮官方 Kconfig 的名称长度默认按 DNS-SD、IPv6 等条件选择，不能只照搬一个与启用功能无关的固定值。依据见[来源记录](../SOURCES.md)。

## 32.3\_网络管理事件（Network Management Events）

解析器发出以下 `NET_MGMT_EVENT` 事件：

| 事件 | 含义 |
| --- | --- |
| [`NET_EVENT_DNS_SERVER_ADD`](https://docs.zephyrproject.org/latest/doxygen/html/group__net__mgmt.html#ga5735d13f24c974ad6d4038c93edf05e0) | 新增一个 DNS 服务器槽位（Slot），每个槽位触发一次，携带来源接口信息。 |
| [`NET_EVENT_DNS_SERVER_DEL`](https://docs.zephyrproject.org/latest/doxygen/html/group__net__mgmt.html#ga9d406772e5d1ad2952b2a2e0fed05c73) | 删除一个服务器槽位，携带来源接口信息。 |
| [`NET_EVENT_DNS_SERVERS_RECONFIGURED`](https://docs.zephyrproject.org/latest/doxygen/html/group__net__mgmt.html#gac654c28128762a3160ce5f5717f053c5) | 经 [`dns_resolve_reconfigure()`](https://docs.zephyrproject.org/latest/doxygen/html/group__dns__resolve.html#ga1d3bb0319531bfe0ae95f48bdc51c56f) 或 [`dns_resolve_reconfigure_with_interfaces()`](https://docs.zephyrproject.org/latest/doxygen/html/group__dns__resolve.html#ga3d22eed1d6d017e5bd7a2344775d33b7) 刷新服务器配置；每次成功调用都会发出，不要求某个槽位确实变化。接口为 `NULL`，表示系统级事件。 |

`ADD` 与 `DEL` 是增量事件（Delta Event）。新服务器集合与原集合相同时，不会触发这两个事件；这是有意避免 DHCP Offer 重传或 IPv6 RA 导致取消正在进行的查询。

如果应用需要在网络事件之后确认“DNS 配置再次就绪”，应监听 [`NET_EVENT_DNS_SERVERS_RECONFIGURED`](https://docs.zephyrproject.org/latest/doxygen/html/group__net__mgmt.html#gac654c28128762a3160ce5f5717f053c5)。例如 PPP 接口重新建立后，在每次电源管理（Power Management，PM）恢复周期中通过 IP 控制协议（IP Control Protocol，IPCP）重新推送同一组 DNS 服务器，此时不能仅依赖 [`NET_EVENT_DNS_SERVER_ADD`](https://docs.zephyrproject.org/latest/doxygen/html/group__net__mgmt.html#ga5735d13f24c974ad6d4038c93edf05e0)。

## 32.4\_示例与 API 参考

具体用法见[DNS 解析示例](P037_DNS解析示例.md#dns-resolve)，详细 API 见[DNS 解析库](https://docs.zephyrproject.org/latest/doxygen/html/group__dns__resolve.html)。相关官方示例还包括：

- [AWS IoT Core MQTT](P216_AWS物联网MQTT示例.md#aws-iot-mqtt)：连接 AWS IoT Core 并使用 MQTT 发布消息。
- [DNS 解析](P037_DNS解析示例.md#dns-resolve)：解析给定主机名的 IP 地址。
- [TagoIO HTTP Post](P218_TagoIO的HTTP上报示例.md#tagoio-http-post)：通过 HTTP 向 TagoIO 物联网云平台发送随机温度值。


<a id="dns-resolve"></a>
<a id="dns-resolve-interface"></a>
<a id="contents"></a>
<a id="id1"></a>
<a id="id2"></a>
<a id="id3"></a>
<a id="id4"></a>
<a id="overview"></a>
<a id="index-0"></a>
<a id="index-1"></a>
<a id="index-2"></a>
<a id="index-3"></a>
<a id="network-management-events"></a>
<a id="sample-usage"></a>
<a id="api-reference"></a>

<!-- reading-navigation:start -->

**主线阅读**

[上一篇：DHCPv6](P031_DHCPv6.md) · [本模块主线目录](../reading/networking.md) · [全部主线](../reading/README.md) · [下一篇：主机名配置](P033_主机名配置.md)

<details>
<summary>原册编号导航（含扩展参考）</summary>

[上一章](P031_DHCPv6.md) · [返回大纲](大纲.md) · [下一章](P033_主机名配置.md)

</details>

<!-- reading-navigation:end -->
