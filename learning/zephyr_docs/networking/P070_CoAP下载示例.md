---
id: learning.zephyr-docs.networking.page-70
title: CoAP下载示例
kind: reference
status: maintained
domains: [zephyr, networking, development]
source_url: https://docs.zephyrproject.org/latest/samples/net/sockets/coap_download/README.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第70章\_CoAP下载示例

原文：[官方页面](https://docs.zephyrproject.org/latest/samples/net/sockets/coap_download/README.html)。读取日期：2026-10-14；保存的 latest 页面及 HTML 摘要见[来源记录](../SOURCES.md)。

## 70.1 概览（Overview）

本示例使用 CoAP 客户端 API 向服务器发出 GET 请求。数据超过单个 CoAP 分组容量时，自动通过分块传输（Blockwise Transfer）接收。传输结束后，打印接收字节数和用时。可[浏览官方源码](https://github.com/zephyrproject-rtos/zephyr/blob/main//samples/net/sockets/coap_download/README.rst/..)。

## 70.2 运行要求（Requirements）

可按[与主机系统联网](P007_与主机系统联网.md#networking-with-host)、[native_sim 联网](P008_native_sim联网.md#networking-with-native-sim)准备模拟网络，或使用带硬件网络接口的开发板。原文在 `nucleo_h753zi` 上测试过；这是上游记录。开发板与运行 CoAP 服务器的主机之间须能通信。

## 70.3 构建与运行（Build and Running）

在 Zephyr 源码根目录构建：

```shell
west build -b <board to use> samples/net/sockets/coap_download -- -DCONF_FILE=<config file to use>
```

将 `<board to use>`、`<config file to use>` 替换为实际开发板和配置文件。最方便的运行方式是 native_sim，先完成对应联网准备。

主机需取得 CoAP 服务器应用，例如 Python 实现的[aiocoap](https://github.com/chrysn/aiocoap)，或 Java 实现的[Eclipse Californium](https://github.com/eclipse-californium/californium)所提供的[简单文件服务器示例](https://github.com/eclipse-californium/californium/tree/main/demo-apps/cf-simplefile-server)。

使用 aiocoap 时，在 Linux 主机选定的可写目录执行：

```shell
python -m pip install "aiocoap[all]"
mkdir file_root
echo "some test data" > file_root/test.txt
aiocoap-fileserver file_root
```

`file_root` 与 `test.txt` 由这些命令创建，前者作为服务器文件根目录。可通过应用 Kconfig 配置修改请求的资源名：

```kconfig
CONFIG_NET_SAMPLE_COAP_RESOURCE_PATH="resource_name_to_request"
```

> 源码核对译注：[`CONFIG_NET_SAMPLE_COAP_RESOURCE_PATH`](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/net/sockets/coap_download/Kconfig) 是本示例 [Kconfig](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/net/sockets/coap_download/Kconfig) 定义的私有选项，默认 `test.txt`。其值是相对服务器文件根目录的资源路径；不要填作者机器上的绝对文件位置。

另开终端，在已取得的 `net-tools` 目录启动 `net-setup.sh`：

```shell
./net-setup.sh
```

然后在 Zephyr 源码根目录构建并运行 native_sim 版本：

```shell
west build -b native_sim samples/net/sockets/coap_download
west build -t run
```

## 70.4 示例输出（Sample Output）

```text
[00:00:00.000,000] <inf> net_config: Initializing network
[00:00:00.000,000] <inf> net_config: IPv4 address: 192.0.2.1
[00:00:00.110,000] <inf> net_config: IPv6 address: 2001:db8::1
[00:00:00.110,000] <inf> net_config: IPv6 address: 2001:db8::1
[00:00:00.110,000] <inf> coap_download: Network L4 is connected
[00:00:00.110,000] <inf> coap_download: Starting CoAP download using IPv4
[00:00:00.180,000] <inf> coap_download: CoAP response, result_code=69, offset=0, len=100
[00:00:00.180,000] <inf> coap_download: CoAP download done, got 100 bytes in 70 ms
[00:00:00.180,000] <inf> coap_download: Starting CoAP download using IPv6
[00:00:00.300,000] <inf> coap_download: CoAP response, result_code=69, offset=0, len=100
[00:00:00.300,000] <inf> coap_download: CoAP download done, got 100 bytes in 120 ms
```

这是官方原页的历史输出，分别展示 IPv4、IPv6 下载 100 字节所用的时间。前面 `echo` 创建的短文件不必得到相同字节数或耗时；`result_code=69` 是 CoAP 编码后的响应码，对应 `2.05 Content`（内容），不是 HTTP 状态码。

## 70.5 相关参考（See Also）

参见[CoAP 基础库 API](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html)及[CoAP 客户端库](P065_CoAP客户端库.md)。本轮未安装服务器、修改网络、构建或执行下载性能测试。


<a id="coap-download"></a>
<a id="overview"></a>
<a id="requirements"></a>
<a id="build-and-running"></a>
<a id="sample-output"></a>
<a id="see-also"></a>

[上一章](P069_CoAP_TCP客户端示例.md) · [返回大纲](大纲.md) · [下一章](P071_CoAP上传示例.md)
