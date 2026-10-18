---
id: learning.zephyr-docs.networking.page-120
title: LLDP示例
kind: reference
status: maintained
domains: [zephyr, networking, development]
source_url: https://docs.zephyrproject.org/latest/samples/net/ethernet/lldp/README.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第120章\_LLDP示例

原文：[官方页面](https://docs.zephyrproject.org/latest/samples/net/ethernet/lldp/README.html)。读取日期：2026-10-14；保存的 latest 页面及 HTML 摘要见[来源记录](../SOURCES.md)。

## 1. 概述（Overview）

Zephyr 的链路层发现协议（Link Layer Discovery Protocol，LLDP）示例启用 LLDP，并在需要时设置 VLAN。

示例源码位于 [`samples/net/ethernet/lldp`](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/net/ethernet/lldp)，可[在 GitHub 查看官方源码](https://github.com/zephyrproject-rtos/zephyr/blob/main//samples/net/ethernet/lldp/README.rst/..)。

## 2. 前提条件（Requirements）

先阅读[与主机系统联网](P007_与主机系统联网.md#networking-with-host)，准备测试所需的连接。

## 3. 构建和运行（Building and Running）

可按[QEMU 联网](P009_QEMU联网概览.md#networking-with-qemu)中的方法在 QEMU 中运行，也可使用 FRDM-K64F 等嵌入式设备。注意，LLDP 仅支持具有以太网端口的开发板。

构建 LLDP 示例：

```sh
west build -b <board to use> samples/net/ethernet/lldp -- -DCONF_FILE=prj.conf
```

> 译注——执行前提：从 Zephyr 源码根目录，在已准备好工具链和依赖的终端中执行，把 `<board to use>` 换成实际板目标。示例和 `prj.conf` 是官方已有文件，构建后按板或 QEMU 的运行方法启动。当前官方 [`src/main.c`](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/net/ethernet/lldp/src/main.c) 检查以太网接口及 `ETHERNET_LLDP` 能力，设置可选 TLV 并登记接收回调。看到“不支持 LLDP”或“找不到以太网接口”的日志时，应回查板和驱动配置；编译成功不代表链路发现已正常工作。

## 4. 设置 Linux 主机（Setting up Linux Host）

如果网络需要 VLAN，可以在 Linux 主机执行官方 [`samples/net/ethernet/vlan/vlan-setup-linux.sh`](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/net/ethernet/vlan/vlan-setup-linux.sh)。脚本创建两个 VLAN，并建立通往 Zephyr 的路由。

> 译注——配套说明：该脚本需要实际父接口名和主机网络管理权限，操作位置及参数见 [VLAN 示例](P112_VLAN示例.md)。这是所选示例的主机网络准备，不要求使用作者的目录或接口名。

## 5. 另请参阅（See Also）

- [LLDP 定义与辅助函数](https://docs.zephyrproject.org/latest/doxygen/html/group__lldp.html)。
- [网络第二层抽象层（Network L2 Abstraction Layer）](https://docs.zephyrproject.org/latest/doxygen/html/group__net__l2.html)。


<a id="lldp"></a>
<a id="overview"></a>
<a id="requirements"></a>
<a id="building-and-running"></a>
<a id="setting-up-linux-host"></a>
<a id="see-also"></a>

[上一章](P119_流量分类.md) · [返回大纲](大纲.md) · [下一章](P121_gPTP示例.md)
