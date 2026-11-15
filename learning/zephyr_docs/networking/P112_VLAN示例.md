---
id: learning.zephyr-docs.networking.page-112
title: VLAN示例
kind: reference
status: maintained
domains: [zephyr, networking, development]
source_url: https://docs.zephyrproject.org/latest/samples/net/ethernet/vlan/README.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第112章\_VLAN示例

原文：[官方页面](https://docs.zephyrproject.org/latest/samples/net/ethernet/vlan/README.html)。读取日期：2026-10-14；保存的 latest 页面及 HTML 摘要见[来源记录](../SOURCES.md)。

## 1. 概述（Overview）

Zephyr 的虚拟局域网（Virtual LAN，VLAN）示例应用建立两个 VLAN 网络。示例启用网络命令行（net-shell），让用户能够查看 VLAN 设置。

示例源码位于 [`samples/net/ethernet/vlan`](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/net/ethernet/vlan)，可[在 GitHub 查看官方源码](https://github.com/zephyrproject-rtos/zephyr/blob/main//samples/net/ethernet/vlan/README.rst/..)。

## 2. 前提条件（Requirements）

先完成[与主机系统联网](P007_与主机系统联网.md#networking-with-host)所述的网络准备。

## 3. 构建和运行（Building and Running）

可以按照[QEMU 以太网联网](P010_QEMU以太网联网.md#networking-with-eth-qemu)中的说明，在 QEMU 中运行此 VLAN 应用。在 Linux 中运行 `net-setup.sh` 时，可使用 `zeth-vlan.conf` 配置文件：

```sh
./net-setup.sh -c zeth-vlan.conf
```

> 译注——命令位置：上面的命令在 Linux Bash 中执行，当前位置为官方外部 `net-tools` 工具的目录，目录内应已有 `net-setup.sh` 与相应配置文件。下载与主机网络准备遵循前面的联网文档；该命令用于准备主机网络，不是编译 Zephyr。

注意：VLAN 仅支持具有以太网端口或支持 USB 联网的开发板。

构建 VLAN 示例应用：

```sh
west build -b <board to use> samples/net/ethernet/vlan -- -DCONF_FILE=prj.conf
```

> 译注——构建前提：在具备 Zephyr 构建环境的终端中，从 Zephyr 源码根目录执行。将 `<board to use>` 替换为具备相应网络支持的实际板目标；示例目录和 `prj.conf` 是官方源码已有文件。构建成功只说明生成了目标程序，运行方式仍按所选板或 QEMU 的说明完成。

默认配置文件 [`samples/net/ethernet/vlan/prj.conf`](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/net/ethernet/vlan/prj.conf) 创建如下两个虚拟局域网：

| VLAN 标签（Tag） | IPv4 地址 | IPv6 地址 |
| --- | --- | --- |
| 100 | `198.51.100.1` | `2001:db8:100::1` |
| 200 | `203.0.113.1` | `2001:db8:200::1` |

> 译注——源码跟踪：当前官方 [`src/main.c`](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/net/ethernet/vlan/src/main.c) 调用 `init_vlan()` 完成示例初始化；配置文件提供所需参数。配置中的两个 VLAN 分别使用 `/24` 的 IPv4 前缀和 `/64` 的 IPv6 前缀。这与“只在编译配置中打开 VLAN 就已完成运行时配置”是不同的。

## 4. 设置 Linux 主机（Setting up Linux Host）

官方脚本 [`samples/net/ethernet/vlan/vlan-setup-linux.sh`](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/net/ethernet/vlan/vlan-setup-linux.sh) 可以在 Linux 主机上执行。它创建 `vlan.100` 和 `vlan.200` 两个 VLAN 接口，并添加通往 Zephyr 的路由。

> 译注——脚本调用前提：官方 [vlan-setup-linux.sh](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/net/ethernet/vlan/vlan-setup-linux.sh) 要求以 root 身份运行，并把实际父接口名作为第一个参数，例如连接目标的以太网接口或已准备好的 TAP 接口名。脚本把主机侧 VLAN 100 配为 `198.51.100.2/24`、`2001:db8:100::2/64`，VLAN 200 配为 `203.0.113.2/24`、`2001:db8:200::2/64`。这些是示例网络地址，不是作者机器上的目录。运行前须先按联网文档确定实际父接口。

如果各项设置正确，在 Linux 主机的 Bash 中执行以下命令应成功收到响应。执行目录不限，但目标应用应已运行，且主机的 VLAN 接口和路由已建立：

```sh
ping -c 1 2001:db8:100::1
ping -c 1 198.51.100.1
ping -c 1 2001:db8:200::1
ping -c 1 203.0.113.1
```

发往 `2001:db8:100::1` 或 `198.51.100.1` 的包携带 VLAN 标签 `100`；发往 `2001:db8:200::1` 或 `203.0.113.1` 的包携带 VLAN 标签 `200`。

> 译注——结果定位：若没有收到响应，先回查父接口连接、两侧 VLAN 标签、地址和路由，再检查应用是否已完成 VLAN 初始化；不能仅凭编译成功判断网络已接通。

## 5. 另请参阅（See Also）

- [虚拟局域网定义与辅助函数](https://docs.zephyrproject.org/latest/doxygen/html/group__vlan__api.html)。
- [网络第二层抽象层（Network L2 Abstraction Layer）](https://docs.zephyrproject.org/latest/doxygen/html/group__net__l2.html)。
- [网络接口抽象层（Network Interface Abstraction Layer）](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html)。


<a id="vlan"></a>
<a id="overview"></a>
<a id="requirements"></a>
<a id="building-and-running"></a>
<a id="setting-up-linux-host"></a>
<a id="see-also"></a>

[上一章](P111_以太网示例目录.md) · [返回大纲](大纲.md) · [下一章](P113_以太网桥示例.md)
