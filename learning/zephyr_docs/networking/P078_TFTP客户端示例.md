---
id: learning.zephyr-docs.networking.page-78
title: TFTP客户端示例
kind: reference
status: maintained
domains: [zephyr, networking, development]
source_url: https://docs.zephyrproject.org/latest/samples/net/tftp_client/README.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第78章\_TFTP客户端示例

原文：[官方页面](https://docs.zephyrproject.org/latest/samples/net/tftp_client/README.html)。读取日期：2026-10-14；保存的 latest 页面及 HTML 摘要见[来源记录](../SOURCES.md)。

## 78.1 概览（Overview）

简单文件传输协议（Trivial File Transfer Protocol，TFTP）是基于用户数据报协议（User Datagram Protocol，UDP）的简单锁步文件传输协议（Lockstep File Transfer Protocol），用于从远端主机取得文件或向其写入文件。

本示例使用 Zephyr TFTP 客户端库，向标准端口 `69` 上的服务器发起传输。源码位于[samples/net/tftp_client](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/net/tftp_client)，也可[浏览官方示例](https://github.com/zephyrproject-rtos/zephyr/blob/main//samples/net/tftp_client/README.rst/..)。

## 78.2 运行要求（Requirements）

需要 Linux 主机，并按[QEMU 以太网联网](P010_QEMU以太网联网.md#networking-with-eth-qemu)、[QEMU 联网](P009_QEMU联网概览.md#networking-with-qemu)或[native_sim 联网](P008_native_sim联网.md#networking-with-native-sim)准备网络。

## 78.3 构建与服务器准备（Building and Running）

示例目录中的 `prj.conf` 是标准默认配置。在 Zephyr 源码根目录构建，替换实际开发板及配置文件参数：

```shell
west build -b <board to use> samples/net/tftp_client -- -DCONF_FILE=<config file to use>
```

最方便的方式是使用默认 `prj.conf` 构建 native_sim 或 QEMU 版本，先完成前面的联网准备。native_sim 的构建和运行命令为：

```shell
west build -b native_sim samples/net/tftp_client
west build -t run
```

主机需下载并运行 TFTP 服务器，例如 TFTPd；在该服务器暴露的文件根目录中创建有数据的 `file1.bin`，以及 `newfile.bin`。

> 译注：虽然原页在构建命令后才描述服务器，首次运行前仍应准备好网络、服务器与两个文件。根据当前[示例源码](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/net/tftp_client/src/tftp-client.c)，程序先以 `octet`（八位字节）模式获取 `file1.bin`，收到数据后打印十六进制内容，再把内置 `TFTP_SAMPLE_DATA` 写入 `newfile.bin`。它不是把下载文件原样再上传，也没有把接收数据保存成设备本地文件。预建目标文件仍须满足服务器自身的写权限策略。

## 78.4 服务器地址与 DNS

默认服务器地址为 `192.0.2.2`，端口为 `69`。修改 `prj.conf` 可指定其他地址和端口：

```kconfig
CONFIG_TFTP_APP_SERVER="10.0.0.10"
CONFIG_TFTP_APP_PORT="70"
```

通过主机名连接时，在 `prj.conf` 启用 DNS 解析器（DNS Resolver）并设置名称：

```kconfig
CONFIG_DNS_RESOLVER=y
CONFIG_TFTP_APP_SERVER="my-tftp-server.org"
```

> 源码核对译注：[`CONFIG_TFTP_APP_SERVER`](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/net/tftp_client/Kconfig) 与 [`CONFIG_TFTP_APP_PORT`](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/net/tftp_client/Kconfig) 定义在示例私有 [Kconfig](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/net/tftp_client/Kconfig)，两者都是字符串，因此端口示例的双引号应保留。源码把服务器名和端口分别传给 `getaddrinfo()`；服务器参数应是主机名或 IP，不要因 Kconfig 帮助里“full URI”的措辞而加上 `tftp://` 或混入端口。DNS 场景还需要可用的解析服务器配置。

## 78.5 示例输出（Sample Output）

主机运行 TFTP 服务器时，客户端可在[native_sim](../native_reference/P004_Native_Simulator本机模拟器.md#native_sim)中运行。原文在 `net-tools` 目录启动网络准备脚本：

```shell
net-setup.sh
```

> 译注：原例直接写 `net-setup.sh`。如果脚本所在目录未加入 `PATH`，在该目录应使用 `./net-setup.sh`。这是主机 Shell 操作，与后面的设备日志分开。

原始输出如下：

```text
<inf> net_config: Initializing network
<inf> net_config: IPv4 address: 192.0.2.1
<inf> net_tftp_client_app: Run TFTP client
<inf> net_tftp_client_app: Received data:
        74 65 73 74 74 66 74 70  66 6f 72 7a 65 70 68 79 |testtftp forzephy
        72 0a                                            |r.
<inf> net_tftp_client_app: TFTP client get done
<inf> net_tftp_client_app: TFTP client put done
```

这里接收内容由服务器上的 `file1.bin` 决定；“get done”和“put done”来自官方原例，不是本轮运行结果。

## 78.6 相关参考（See Also）

参见[TFTP 客户端库 API](P084_TFTP完整API参考.md)。本轮未安装服务器、设置网络、构建或读写任何远端文件。


<a id="tftp-client"></a>
<a id="overview"></a>
<a id="requirements"></a>
<a id="building-and-running"></a>
<a id="sample-output"></a>
<a id="see-also"></a>

[上一章](P077_TFTP客户端库.md) · [返回大纲](大纲.md) · [下一章](P079_SOCKS5代理支持.md)
