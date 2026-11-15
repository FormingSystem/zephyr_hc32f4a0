---
id: learning.zephyr-docs.networking.page-71
title: CoAP上传示例
kind: reference
status: maintained
domains: [zephyr, networking, development]
source_url: https://docs.zephyrproject.org/latest/samples/net/sockets/coap_upload/README.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第71章\_CoAP上传示例

原文：[官方页面](https://docs.zephyrproject.org/latest/samples/net/sockets/coap_upload/README.html)。读取日期：2026-10-14；保存的 latest 页面及 HTML 摘要见[来源记录](../SOURCES.md)。

## 71.1 概览（Overview）

本示例使用 CoAP 客户端 API，通过 PUT 请求向服务器上传内容，展示四种方式：

- 使用负载指针（Payload Pointer）上传短数据。
- 使用负载回调（Payload Callback）上传短数据。
- 使用负载指针进行分块上传（Blockwise Upload）。
- 使用负载回调进行分块上传。

示例可与[CoAP 服务示例](P072_CoAP服务示例.md#coap-server)配合，也可连接独立服务器，例如[aiocoap](https://github.com/chrysn/aiocoap)。可[浏览官方源码](https://github.com/zephyrproject-rtos/zephyr/blob/main//samples/net/sockets/coap_upload/README.rst/..)。

## 71.2 运行要求（Requirements）

按[与主机系统联网](P007_与主机系统联网.md#networking-with-host)、[native_sim 联网](P008_native_sim联网.md#networking-with-native-sim)准备模拟网络，或使用带硬件网络接口的开发板。原文在 `nrf7002dk` 上配合 `wifi-ipv4` 配置片段（Snippet）测试过；这是上游测试记录。

开发板与运行 CoAP 服务器的主机之间须有可用网络连接。

## 71.3 构建与运行（Build and Running）

在 Zephyr 源码根目录构建；将 `<board to use>` 替换为实际目标：

```shell
west build -b <board to use> samples/net/sockets/coap_upload
```

最方便的方式是运行 native_sim 版本，先完成 native_sim 联网指南中的准备。主机需取得服务器应用，例如 Python 实现的 aiocoap。

在 Linux 主机选定的可写工作目录执行下面的原始命令：

```shell
python -m pip install "aiocoap[all]"
mkdir file_root
aiocoap-fileserver --write file_root
```

`file_root` 是命令新建的服务器根目录；`--write` 允许服务器接受写入，使 PUT 可以上传内容。

另开终端，在已取得的 `net-tools` 目录启动 `net-setup.sh`：

```shell
./net-setup.sh
```

再在 Zephyr 源码根目录构建并运行上传示例：

```shell
west build -b native_sim samples/net/sockets/coap_upload
west build -t run
```

## 71.4 示例输出（Sample Output）

```text
[00:00:00.000,000] <inf> net_config: Initializing network
[00:00:00.000,000] <inf> net_config: IPv4 address: 192.0.2.1
[00:00:00.110,000] <inf> net_config: IPv6 address: 2001:db8::1
[00:00:00.110,000] <inf> net_config: IPv6 address: 2001:db8::1
[00:00:00.110,000] <inf> net_samples_common: Network connectivity established and IP address assigned
[00:00:00.110,000] <inf> net_samples_common: Waiting for network...
[00:00:00.110,000] <inf> coap_upload:
[00:00:00.110,000] <inf> coap_upload: * Starting CoAP upload using IPv4
[00:00:00.110,000] <inf> coap_upload:
[00:00:00.110,000] <inf> coap_upload: ** CoAP upload short
[00:00:00.180,000] <inf> coap_upload: CoAP upload short done in 70 ms
[00:00:00.180,000] <inf> coap_upload:
[00:00:00.180,000] <inf> coap_upload: ** CoAP upload short with callback
[00:00:00.240,000] <inf> coap_upload: CoAP upload short with callback done in 60 ms
[00:00:00.240,000] <inf> coap_upload:
[00:00:00.240,000] <inf> coap_upload: ** CoAP upload blockwise
[00:00:00.300,000] <inf> coap_upload: CoAP upload blockwise ongoing, sent 128 bytes so far
[00:00:00.360,000] <inf> coap_upload: CoAP upload blockwise ongoing, sent 256 bytes so far
[00:00:00.420,000] <inf> coap_upload: CoAP upload blockwise ongoing, sent 384 bytes so far
[00:00:00.480,000] <inf> coap_upload: CoAP upload blockwise done in 240 ms
[00:00:00.480,000] <inf> coap_upload:
[00:00:00.480,000] <inf> coap_upload: ** CoAP upload blockwise with callback
[00:00:00.540,000] <inf> coap_upload: CoAP upload blockwise with callback ongoing, sent 128 bytes so far
[00:00:00.600,000] <inf> coap_upload: CoAP upload blockwise with callback ongoing, sent 256 bytes so far
[00:00:00.660,000] <inf> coap_upload: CoAP upload blockwise with callback ongoing, sent 384 bytes so far
[00:00:00.720,000] <inf> coap_upload: CoAP upload blockwise with callback done in 240 ms
[00:00:01.230,000] <inf> coap_upload:
[00:00:01.230,000] <inf> coap_upload: * Starting CoAP upload using IPv6
[00:00:01.230,000] <inf> coap_upload:
[00:00:01.230,000] <inf> coap_upload: ** CoAP upload short
[00:00:01.320,000] <inf> coap_upload: CoAP upload short done in 90 ms
[00:00:01.320,000] <inf> coap_upload:
[00:00:01.320,000] <inf> coap_upload: ** CoAP upload short with callback
[00:00:01.380,000] <inf> coap_upload: CoAP upload short with callback done in 60 ms
[00:00:01.380,000] <inf> coap_upload:
[00:00:01.380,000] <inf> coap_upload: ** CoAP upload blockwise
[00:00:01.440,000] <inf> coap_upload: CoAP upload blockwise ongoing, sent 128 bytes so far
[00:00:01.500,000] <inf> coap_upload: CoAP upload blockwise ongoing, sent 256 bytes so far
[00:00:01.560,000] <inf> coap_upload: CoAP upload blockwise ongoing, sent 384 bytes so far
[00:00:01.620,000] <inf> coap_upload: CoAP upload blockwise done in 240 ms
[00:00:01.620,000] <inf> coap_upload:
[00:00:01.620,000] <inf> coap_upload: ** CoAP upload blockwise with callback
[00:00:01.680,000] <inf> coap_upload: CoAP upload blockwise with callback ongoing, sent 128 bytes so far
[00:00:01.740,000] <inf> coap_upload: CoAP upload blockwise with callback ongoing, sent 256 bytes so far
[00:00:01.800,000] <inf> coap_upload: CoAP upload blockwise with callback ongoing, sent 384 bytes so far
[00:00:01.860,000] <inf> coap_upload: CoAP upload blockwise with callback done in 240 ms
```

上述官方原页日志先使用 IPv4，再使用 IPv6；每种地址族分别展示四种上传方式、分块进度与完成耗时。字节数、时间戳和耗时原样保留，不代表本轮实测。

## 71.5 相关参考（See Also）

参见[CoAP 基础库 API](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html)；负载回调的偏移、长度和生命周期说明见[CoAP 客户端库](P065_CoAP客户端库.md)。本轮未启动服务器、写入远端文件、构建或运行上传测试。


<a id="coap-upload"></a>
<a id="overview"></a>
<a id="requirements"></a>
<a id="build-and-running"></a>
<a id="sample-output"></a>
<a id="see-also"></a>

[上一章](P070_CoAP下载示例.md) · [返回大纲](大纲.md) · [下一章](P072_CoAP服务示例.md)
