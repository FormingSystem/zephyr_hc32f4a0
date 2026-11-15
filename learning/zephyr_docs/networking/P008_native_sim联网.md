---
id: learning.zephyr-docs.networking.page-8
title: native_sim联网
kind: reference
status: maintained
domains: [zephyr, networking, development]
source_url: https://docs.zephyrproject.org/latest/services/connectivity/networking/native_sim_setup.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第8章\_native_sim联网

原文：[官方页面](https://docs.zephyrproject.org/latest/services/connectivity/networking/native_sim_setup.html)。读取日期：2026-10-14；保存的 latest 页面及 HTML 摘要见[来源记录](../SOURCES.md)。

## 8.1\_使用虚拟TAP以太网驱动

本节说明如何在 Linux 主机与运行于 [native_sim](../native_reference/P004_Native_Simulator本机模拟器.md#native_sim) 开发板的 Zephyr 应用之间建立虚拟网络。示例运行Zephyr源码中的 [高级回显服务器（Echo Server）](P047_高级回显服务器示例.md#sockets-echo-server)，经 Linux 中表现为以太网接口的 tuntap 设备与主机连接。

### 8.1.1\_前置条件

在Linux主机找到Zephyr的 [网络工具项目（net-tools）](https://github.com/zephyrproject-rtos/net-tools)。标准工作区可能已在 `tools/net-tools` 中提供；也可从其独立Git仓库取得：

```sh
git clone https://github.com/zephyrproject-rtos/net-tools
```

以下需要三个终端：终端1位于 [`net-tools`](https://github.com/zephyrproject-rtos/net-tools) 目录，即先执行 `cd net-tools`；终端2为已初始化Zephyr环境的开发终端；终端3用于运行中的native_sim控制台，可选。

### 8.1.2\_创建以太网接口

启动带网络仿真的native_sim前，先在终端1创建主机网络接口：

```sh
./net-setup.sh
```

可调整脚本行为，选项见帮助：

```sh
./net-setup.sh --help
```

### 8.1.3\_启动应用

在终端2构建并启动 `echo_server` 示例：

```sh
west build -b native_sim samples/net/sockets/echo_server
west build -t run
```

译注：相对的 `samples/...` 从Zephyr源码根解析，`west build -t run` 使用刚生成的构建目录。本页没有要求使用作者电脑上的固定仓库位置。

### 8.1.4\_连接控制台

Zephyr启动时通常自动打开控制台。如果没有打开，native_sim会打印类似下面的伪终端（Pseudoterminal）信息：

```text
UART connected to pseudotty: /dev/pts/5
```

可手动连接：

```sh
screen /dev/pts/5
```

译注：`/dev/pts/5` 是本次运行输出的Linux设备节点示例，应以实际输出为准；它不是作者仓库路径。

## 8.2\_使用卸载套接字

与TAP方案相比，卸载套接字（Offloaded Sockets）的主要优点是无需在主机创建虚拟网络接口，因此无需提升到root权限。

### 8.2.1\_启动native_sim应用

在Zephyr开发终端构建并启动回显服务器：

```sh
west build -b native_sim samples/net/sockets/echo_server -- -DEXTRA_CONF_FILE=overlay-nsos.conf
west build -t run
```

### 8.2.2\_运行net-tools回显客户端

Linux主机可使用工作区 `tools/net-tools`，也可单独克隆：

```sh
git clone https://github.com/zephyrproject-rtos/net-tools
```

**原文注意（Note）**：使用卸载套接字驱动的Native Simulator，与其他使用BSD套接字API的Linux应用共享网络接口／命名空间（Namespace）。因此回显服务器与 `echo-client` 通过本地主机／环回接口（Localhost / Loopback）地址 `127.0.0.1` 通信。

进入net-tools目录后，UDP测试为：

```sh
./echo-client 127.0.0.1
```

TCP测试为：

```sh
./echo-client -t 127.0.0.1
```

译注：若克隆后尚没有 `echo-client` 可执行文件，需要先按net-tools项目的构建说明生成它。回显成功应能看到客户端收发结果；以上为官方操作说明，本轮未实际运行网络测试。

## 8.3\_从命令行设置接口和IPv4参数

默认以太网接口名由 `zephyr,native-tap` 设备树节点的 `host-interface` 属性决定，也可用 `--eth-if=<interface_name>` 设置。IPv4地址、网关（Gateway）和掩码（Netmask）分别可由 `--ipv4-addr=<ip_address>`、`--ipv4-gw=<gateway>`、`--ipv4-nm=<netmask>` 设置。

这些选项应用于第一个接口。定义多个 `zephyr,native-tap` 接口时，其余接口具有以设备树节点名为前缀的独立选项，例如 `--<node>_eth-if`、`--<node>_ipv4-addr`。

[`CONFIG_NET_CONFIG_MY_IPV4_ADDR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_CONFIG_MY_IPV4_ADDR) 与命令行参数同时生效；两者都设置时，接口可能最终拥有两个IP地址，通常只选一种设置方式更合适。这对运行多个实例、又不希望逐实例重新编译很有用。

原文示例：

```sh
./zephyr.exe --eth-if=zeth2 --ipv4-addr=192.0.2.2 --ipv4-gw=192.0.0.1
--ipv4-nm=255.255.0.0
```

> 译注：原代码在 `--ipv4-nm` 前换行，却没有Shell续行符。复制执行时应把全部参数放在同一行，或显式加反斜杠续行；例如下面从已生成的Zephyr可执行文件所在目录执行：

```sh
./zephyr.exe --eth-if=zeth2 --ipv4-addr=192.0.2.2 --ipv4-gw=192.0.0.1 \
  --ipv4-nm=255.255.0.0
```

**原文注意（Note）**：也可在构建时通过 [`CONFIG_NATIVE_EXTRA_CMDLINE_ARGS`](../../../boards/native/common/extra_args/Kconfig) 提供这些命令行选项。


> 源码跟踪译注：接口参数读取可对照 [`eth_native_tap.c`](../../../drivers/ethernet/eth_native_tap.c)，额外启动参数定义见 [`boards/native/common/extra_args/Kconfig`](../../../boards/native/common/extra_args/Kconfig)。该配置在本次读取的官方源码中存在；本地 Kconfig 网页符号数据库未定位到它，故提供实际源码入口。所读取官方文件摘要见[来源记录](../SOURCES.md)，不将本仓库源码自动当作 latest 的同版本副本。


<a id="networking-with-native-sim-board"></a>
<a id="networking-with-native-sim"></a>
<a id="contents"></a>
<a id="id1"></a>
<a id="id2"></a>
<a id="id3"></a>
<a id="id4"></a>
<a id="id5"></a>
<a id="id6"></a>
<a id="id7"></a>
<a id="using-virtual-tap-ethernet-driver"></a>
<a id="prerequisites"></a>
<a id="basic-setup"></a>
<a id="step-1-create-ethernet-interface"></a>
<a id="step-2-start-app-in-native-sim-board"></a>
<a id="step-3-connect-to-console-optional"></a>
<a id="using-offloaded-sockets"></a>
<a id="step-1-start-app-in-native-sim-board"></a>
<a id="step-2-run-echo-client-from-net-tools"></a>
<a id="setting-interface-name-and-ipv4-parameters-from-command-line"></a>

<!-- reading-navigation:start -->

**主线阅读**

[上一篇：与主机系统联网](P007_与主机系统联网.md) · [本模块主线目录](../reading/networking.md) · [全部主线](../reading/README.md) · [下一篇：QEMU联网概览](P009_QEMU联网概览.md)

<details>
<summary>原册编号导航（含扩展参考）</summary>

[上一章](P007_与主机系统联网.md) · [返回大纲](大纲.md) · [下一章](P009_QEMU联网概览.md)

</details>

<!-- reading-navigation:end -->
