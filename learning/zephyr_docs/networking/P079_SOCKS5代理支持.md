---
id: learning.zephyr-docs.networking.page-79
title: SOCKS5代理支持
kind: reference
status: maintained
domains: [zephyr, networking, development]
source_url: https://docs.zephyrproject.org/latest/services/connectivity/networking/api/socks5.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第79章\_SOCKS5代理支持

原文：[官方页面](https://docs.zephyrproject.org/latest/services/connectivity/networking/api/socks5.html)。读取日期：2026-10-14；保存的 latest 页面及 HTML 摘要见[来源记录](../SOURCES.md)。

## 79.1 概览（Overview）

SOCKS 库实现 SOCKS5 支持，使 Zephyr 可通过网络代理（Network Proxy）连接对端设备。原文的工作原理介绍见[SOCKS5 百科条目](https://en.wikipedia.org/wiki/SOCKS#SOCKS5)，协议定义见[RFC 1928](https://datatracker.ietf.org/doc/html/rfc1928.html)。

## 79.2 SOCKS5 API

通过 [`CONFIG_SOCKS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOCKS) 启用。应用需要调用 [`setsockopt()`](https://docs.zephyrproject.org/latest/doxygen/html/posix_2sys_2socket_8h.html#a71c8788caef89a362e35ce5855e77077) 设置代理主机地址：

```c
static int set_proxy(int sock, const struct sockaddr *proxy_addr,
                     socklen_t proxy_addrlen)
{
    int ret;

    ret = setsockopt(sock, SOL_SOCKET, SO_SOCKS5,
                     proxy_addr, proxy_addrlen);
    if (ret < 0) {
            return -errno;
    }

    return 0;
}
```

`proxy_addr` 和 `proxy_addrlen` 表示代理地址及其长度。示例在失败时将套接字错误 `errno` 转为负值返回，成功返回 0。

> 源码核对译注：当前官方 [`socks.c`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/socks/socks.c) 仅协商无需认证（NOAUTH）的方式，使用 `CONNECT` 命令，并要求流式套接字（Stream Socket）；实现注释说明支持 TCP／TLS，尚不支持 UDP／DTLS。不能把“支持 SOCKS5”理解为所有认证方法和代理命令均已实现。

## 79.3 MQTT 中的代理用法（SOCKS5 Proxy Usage in MQTT）

MQTT 客户端提供 `mqtt_client_set_proxy()`，应用可通过该接口设置 SOCKS5 代理。具体用法见[MQTT 发布者示例](P060_MQTT发布者示例.md#mqtt-publisher)。本轮未建立代理、连接对端或执行 MQTT 发布。


<a id="socks5-proxy-support"></a>
<a id="socks5-interface"></a>
<a id="contents"></a>
<a id="id1"></a>
<a id="id2"></a>
<a id="id3"></a>
<a id="overview"></a>
<a id="index-0"></a>
<a id="socks5-api"></a>
<a id="socks5-proxy-usage-in-mqtt"></a>

<!-- reading-navigation:start -->

**主线阅读**

[上一篇：TFTP客户端库](P077_TFTP客户端库.md) · [本模块主线目录](../reading/networking.md) · [全部主线](../reading/README.md) · [下一篇：网络Shell](P092_网络Shell.md)

<details>
<summary>原册编号导航（含扩展参考）</summary>

[上一章](P078_TFTP客户端示例.md) · [返回大纲](大纲.md) · [下一章](P080_FTP完整API参考.md)

</details>

<!-- reading-navigation:end -->
