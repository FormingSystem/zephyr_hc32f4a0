---
id: learning.zephyr-docs.networking.page-72
title: CoAP服务示例
kind: reference
status: maintained
domains: [zephyr, networking, development]
source_url: https://docs.zephyrproject.org/latest/samples/net/sockets/coap_server/README.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第72章\_CoAP服务示例

原文：[官方页面](https://docs.zephyrproject.org/latest/samples/net/sockets/coap_server/README.html)。读取日期：2026-10-14；保存的 latest 页面及 HTML 摘要见[来源记录](../SOURCES.md)。

## 72.1 概览（Overview）

本示例把 CoAP 资源（Resource）注册到一个主服务（Service）。服务器实现要求所有服务和资源在编译期（Compile Time）已知，因为它们会被放入专用链接段（Linker Section）。资源根据所属服务名进入相应段，因此需要链接文件，可参照示例中的 `sections-ram.ld`。可[浏览官方源码](https://github.com/zephyrproject-rtos/zephyr/blob/main//samples/net/sockets/coap_server/README.rst/..)。

所选平台须具备网络支持，必要时调整配置。原文说明，示例在为 CoAP 节点保留的站点本地 IPv6 组播地址（Site-local IPv6 Multicast Address）上监听，默认 UDP 端口为 `5683`；安全 CoAP 使用 `5684`。

> 源码核对译注：当前官方 [`src/main.c`](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/net/sockets/coap_server/src/main.c) 的 `ALL_NODES_LOCAL_COAP_MCAST` 实际为 `ff02::fd`，是链路本地（Link-local）范围，与原页“站点本地”措辞不同。服务绑定任意地址；加入组播的代码仅在非安全服务且启用 IPv6 时编入，不能据原段落推断 DTLS 服务也加入了同一组播组。

示例导出以下资源：

```text
/test
/seg1/seg2/seg3
/query
/separate
/large
/location-query
/large-update
```

这些资源可供欧洲电信标准协会（European Telecommunications Standards Institute，ETSI）相当一部分 CoAP 测试用例使用。

## 72.2 构建与运行（Building and Running）

在 Zephyr 源码根目录构建，替换实际开发板参数：

```shell
west build -b <board to use> samples/net/sockets/coap_server
```

如需安全资源，使用[overlay-dtls.conf](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/net/sockets/coap_server/overlay-dtls.conf)叠加配置启用数据报传输层安全（Datagram Transport Layer Security，DTLS）。

原文说成功时程序没有输出，可以使用 `tcpdump`、`wireshark` 等外部工具验证功能。网络准备见[net-tools](https://github.com/zephyrproject-rtos/net-tools)，并可按[与主机系统联网](P007_与主机系统联网.md#networking-with-host)在 QEMU 或 native_sim 上运行。

> 译注：“没有输出”是原页对示例的描述，实际仍可能出现所启用模块的日志。确认功能应依据请求和响应，而不是仅依据串口安静或出现一条启动日志。

主机可使用[libcoap](https://github.com/obgm/libcoap)实现的 ETSI 测试用例。下面命令在 libcoap 源码根目录运行，`tap0` 和 IPv6 地址须对应实际测试网络：

```shell
sudo ./examples/etsi_coaptest.sh -i tap0 2001:db8::1
```

原文还说明，若使用 TI CC2520 无线收发器，可使用随附的 `prj_cc2520.conf` 启用 IEEE 802.15.4。

> 源码核对译注：读取时的[官方示例目录](https://github.com/zephyrproject-rtos/zephyr/tree/main/samples/net/sockets/coap_server)已没有 `prj_cc2520.conf`，对应原始文件地址返回 404。这里保留原文历史说明，不将这个配置标记为当前随附文件，也不把其他无线叠加配置当成它的等价替代。使用该硬件前应依据当前板级和驱动配置核对。

## 72.3 Wi-Fi

可通过[Wi-Fi 配置片段（Snippet）](../snippets/P027_WiFi_IPv4配置片段.md#snippet-wifi-ipv4)启用 IPv4 Wi-Fi 支持。

## 72.4 相关参考（See Also）

参见[CoAP 基础库 API](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html)和[CoAP 服务 API](https://docs.zephyrproject.org/latest/doxygen/html/group__coap__service.html)。本轮未构建、烧录、运行 QEMU、加入主机组播或进行 DTLS／无线／ETSI 测试。


<a id="coap-server"></a>
<a id="overview"></a>
<a id="building-and-running"></a>
<a id="wi-fi"></a>
<a id="see-also"></a>

[上一章](P071_CoAP上传示例.md) · [返回大纲](大纲.md) · [下一章](P073_LwM2M协议栈.md)
