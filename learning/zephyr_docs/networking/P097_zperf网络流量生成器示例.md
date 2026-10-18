---
id: learning.zephyr-docs.networking.page-97
title: zperf网络流量生成器示例
kind: reference
status: maintained
domains: [zephyr, networking, development]
source_url: https://docs.zephyrproject.org/latest/samples/net/zperf/README.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第97章\_zperf网络流量生成器示例

原文：[官方页面](https://docs.zephyrproject.org/latest/samples/net/zperf/README.html)。读取日期：2026-10-14；保存的 latest 页面及 HTML 摘要见[来源记录](../SOURCES.md)。

## 97.1\_说明与功能

[在GitHub浏览官方示例源码](https://github.com/zephyrproject-rtos/zephyr/tree/main/samples/net/zperf)。

本示例演示[zperf Shell工具](P096_zperf网络流量生成器.md#zperf)，用于评估网络带宽（Network Bandwidth）。

- 兼容iPerf v2.0.10及更新版本；更早版本需要启用[`CONFIG_NET_ZPERF_LEGACY_HEADER_COMPAT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_ZPERF_LEGACY_HEADER_COMPAT)。
- 使用`overlay-iperf3.conf`构建时，会启用[`CONFIG_NET_ZPERF_IPERF3`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_ZPERF_IPERF3)，改为兼容iperf3。
- 无需修改源码，即可使用客户端或服务器模式（Client／Server Mode）。

## 97.2\_支持的平台

zperf不依赖特定开发板（Board-agnostic），但目标平台必须提供Zephyr支持的网络接口。官方说明记录该示例已在以下平台测试：

- Freedom Board（FRDM K64F）。
- QEMU x86。
- Arm FVP BaseR AEMv8-R。
- ARM BASE RevC AEMv8A Fixed Virtual Platforms。

为取得较好性能，示例配置了大量网络数据包对象与缓冲区，因此随机存取存储器（Random Access Memory，RAM）需求较大。如果示例无法装入目标平台RAM，应降低以下配置项的值：

```kconfig
CONFIG_NET_PKT_RX_COUNT=40
CONFIG_NET_PKT_TX_COUNT=40
CONFIG_NET_BUF_RX_COUNT=160
CONFIG_NET_BUF_TX_COUNT=160
```

> 译注：上方是原页给出的配置值，降低多少应结合目标内存与预期负载决定；该测试平台列表也不表示本次已在这些平台运行。

## 97.3\_要求与用法

主机安装iPerf 2.0.10或更新版本；使用`overlay-iperf3.conf`构建时，主机改为使用iperf3。还需具备支持的开发板。根据所选网络技术，可能需要额外设置网络环境。

库的用法见[zperf库文档](P096_zperf网络流量生成器.md#zperf)。

### iperf3

要与iperf3测量，应使用对应的叠加配置（Overlay Configuration）。zperf命令不变，默认端口改为5201。以下命令从Zephyr源码根执行，`<board>`替换为所用目标：

```bash
# From the root of the zephyr repository
west build -b <board> samples/net/zperf -- -DEXTRA_CONF_FILE=overlay-iperf3.conf
west flash
```

此后，设备上的`zperf tcp download`和`zperf udp download`可响应主机的`iperf3 -c <device address>`；设备上的`zperf tcp upload <host address>`可对主机运行的`iperf3 -s`发起测试。地址占位符需替换为实际设备或主机地址。

### 确定性吞吐量回归测试

如果需要与硬件无关、与主机运行速度无关的网络吞吐量回归检测（Throughput Regression Detection），可使用`qemu_x86`、QEMU指令计数（Instruction Counting，icount）模式和客户机内部回环接口。详见[zperf确定性回环吞吐量测试](P098_zperf确定性回环吞吐量.md#zperf-loopback-icount)。

### Wi-Fi

可以通过[Wi-Fi配置片段](../snippets/P027_WiFi_IPv4配置片段.md#snippet-wifi-ipv4)为示例启用IPv4 Wi-Fi支持。

## 97.4\_另见

[网络配置库](https://docs.zephyrproject.org/latest/doxygen/html/group__net__config.html)。


<a id="zperf"></a>
<a id="description"></a>
<a id="features"></a>
<a id="supported-boards"></a>
<a id="requirements"></a>
<a id="usage"></a>
<a id="iperf3"></a>
<a id="deterministic-throughput-regression-testing"></a>
<a id="wi-fi"></a>
<a id="see-also"></a>

[上一章](P096_zperf网络流量生成器.md) · [返回大纲](大纲.md) · [下一章](P098_zperf确定性回环吞吐量.md)
