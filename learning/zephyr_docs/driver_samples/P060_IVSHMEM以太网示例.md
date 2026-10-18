---
id: learning.zephyr-docs.driver_samples.page-60
title: IVSHMEM以太网示例
kind: reference
status: maintained
domains: [zephyr, driver_samples, documentation]
source_url: https://docs.zephyrproject.org/latest/samples/drivers/ethernet/eth_ivshmem/README.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

<a id="eth-ivshmem"></a>

# 第60章\_IVSHMEM以太网示例

原文：[官方页面](https://docs.zephyrproject.org/latest/samples/drivers/ethernet/eth_ivshmem/README.html)。读取日期：2026-10-14；保存的latest页面及HTML摘要见[来源记录](../SOURCES.md)。

<a id="overview"></a>

## 60.1 概述（Overview）

本应用演示如何使用虚拟机间共享内存（Inter-VM Shared Memory，IVSHMEM）以太网，与Jailhouse虚拟机监控器（Hypervisor）中的另一个隔离单元（Cell）通信。目前仅支持`qemu_cortex_a53`开发板。

<a id="building-jailhouse-linux-for-qemu"></a>

## 60.2 为QEMU构建Jailhouse Linux（Building Jailhouse Linux for QEMU）

克隆Jailhouse的Yocto项目。原文编写时，`next`分支包含一些尚未进入`master`分支的修复：

```sh
git clone https://github.com/siemens/jailhouse-images.git
cd jailhouse-images
git switch --detach origin/next
```

打开菜单，选择“QEMU ARM64 virtual target”，然后选择“Save & Build”（保存并构建）。这一过程需要一段时间：

```sh
./kas-container menu
```

编辑`start-qemu.sh`：

- 在`arm64|aarch64`分支中，将`-cpu cortex-a57`改为`-cpu cortex-a53`。
- 在QEMU进程参数的`-netdev user,id=net`后追加`,hostfwd=tcp::2222-:22`，以允许SSH访问。`2222`可以替换成任意未占用端口。

启动QEMU：

```sh
./start-qemu.sh arm64
```

这应当启动Linux并进入Shell。

<a id="build-the-zephyr-sample"></a>

## 60.3 构建Zephyr示例（Build the Zephyr sample）

在Zephyr源码根目录执行原构建命令：

```sh
# From the root of the zephyr repository
west build -b qemu_cortex_a53 samples/drivers/ethernet/eth_ivshmem
```

<a id="running-the-sample"></a>

## 60.4 运行示例（Running the sample）

把生成的`zephyr.bin`复制到Jailhouse Linux的根单元（Root Cell）：

```sh
scp -P 2222 path/to/zephyr.bin root@localhost:/root
```

Jailhouse提供适用于本示例的预制Zephyr单元配置`qemu-arm64-zephyr-demo`。

回到Jailhouse Linux Shell，创建Zephyr单元：

```sh
jailhouse enable /etc/jailhouse/qemu-arm64.cell
jailhouse console
jailhouse cell create /etc/jailhouse/qemu-arm64-zephyr-demo.cell
```

这里可能遇到Linux Shell不再接受输入的现象。如果发生这种情况，通过SSH打开第二个Shell：

```sh
ssh -p 2222 root@localhost
```

加载并启动Zephyr单元：

```sh
jailhouse cell load qemu-arm64-zephyr-demo zephyr.bin --address 0x70000000
jailhouse cell start qemu-arm64-zephyr-demo
```

现在可以运行Zephyr和Linux的Shell命令，在两个单元之间通信。

> 译注——执行位置：克隆、镜像构建、启动QEMU和`scp`属于主机操作；`jailhouse`命令在来宾Linux中执行。`path/to/zephyr.bin`是待替换的构建产物位置；`/root`和`/etc/jailhouse/`是来宾Linux内的目录，`0x70000000`是该单元配置使用的装载地址，均不是作者仓库的绝对路径。不要把这组地址或配置直接套用到其他板型。

<a id="ping-linux-from-zephyr"></a>

### 60.4.1 从Zephyr ping Linux（Ping Linux from Zephyr）

```text
*** Booting Zephyr OS build v3.3.0-475-g45b9e84c6013 ***
uart:~$ net ping 192.168.19.1
PING 192.168.19.1
28 bytes from 192.168.19.1 to 192.168.19.2: icmp_seq=1 ttl=64 time=5.06 ms
28 bytes from 192.168.19.1 to 192.168.19.2: icmp_seq=2 ttl=64 time=7.99 ms
28 bytes from 192.168.19.1 to 192.168.19.2: icmp_seq=3 ttl=64 time=1.77 ms
```

<a id="ping-zephyr-from-linux"></a>

### 60.4.2 从Linux ping Zephyr（Ping Zephyr from Linux）

```text
root@demo:~# ping -c 3 192.168.19.2
PING 192.168.19.2 (192.168.19.2) 56(84) bytes of data.
64 bytes from 192.168.19.2: icmp_seq=1 ttl=64 time=0.646 ms
64 bytes from 192.168.19.2: icmp_seq=2 ttl=64 time=1.45 ms
64 bytes from 192.168.19.2: icmp_seq=3 ttl=64 time=1.28 ms

--- 192.168.19.2 ping statistics ---
3 packets transmitted, 3 received, 0% packet loss, time 2006ms
rtt min/avg/max/mdev = 0.646/1.124/1.450/0.345 ms
```

<a id="run-zperf-iperf"></a>

### 60.4.3 运行zperf／iPerf（Run zperf / iPerf）

可以使用[zperf网络流量生成器（Network Traffic Generator）](../networking/P096_zperf网络流量生成器.md#zperf)／iPerf测量网络吞吐量。

在Zephyr中：

```sh
# Start zperf TCP server
zperf tcp download 5001
```

在Linux中：

```sh
# Install iPerf 2.0.5
apt install wget
wget https://iperf.fr/download/ubuntu/iperf_2.0.5+dfsg1-2_arm64.deb
apt install ./iperf_2.0.5+dfsg1-2_arm64.deb
rm iperf_2.0.5+dfsg1-2_arm64.deb

# Connect iPerf TCP client
iperf -l 1K -V -c 192.168.19.2 -p 5001
```

Zephyr输出：

```text
TCP server started on port 5001
New TCP session started.
TCP session ended
 Duration:              10.01 s
 rate:                  57.72 Mbps
```

Linux输出：

```text
------------------------------------------------------------
Client connecting to 192.168.19.2, TCP port 5001
TCP window size: 85.0 KByte (default)
------------------------------------------------------------
[  3] local 192.168.19.1 port 58430 connected with 192.168.19.2 port 5001
[ ID] Interval       Transfer     Bandwidth
[  3]  0.0-10.0 sec  72.2 MBytes  60.6 Mbits/sec
```

> 译注——配置与测量边界：上述地址、版本和速率来自官方示例记录，不能当作当前仓库的实测结果。当前官方[prj.conf](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/drivers/ethernet/eth_ivshmem/prj.conf)设置Zephyr IPv4地址为`192.168.19.2`、掩码为`255.255.255.0`，并启用网络Shell及zperf服务端。Linux侧地址与隔离单元的网络条件仍需由对应镜像提供；原文固定版本iPerf安装步骤和`next`分支说明按来源保留。

<a id="see-also"></a>

## 60.5 另请参阅（See also）

- [虚拟机间共享内存（Inter-VM Shared Memory）](../intercore_reference/P214_IVSHMEM共享内存接口.md)。
- [以太网支持函数（Ethernet Support Functions）](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet.html)。


对应官方文档源码：[samples/drivers/ethernet/eth_ivshmem/README.rst](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/drivers/ethernet/eth_ivshmem/README.rst)。

> 译注——源码跟踪：本仓库的[对应源码](../../../samples/drivers/ethernet/eth_ivshmem/README.rst)可用于对照，版本可能与网页不同。源码跟踪和实现依据不绑定作者机器目录；项目环境与实验路线另见[项目实验补充](../../zephyr_project_notes/README.md)。

> 译注——示例实现：仓库内的[main.c](../../../samples/drivers/ethernet/eth_ivshmem/src/main.c)用于实现跟踪；它可能与上方网页及main分支版本不同。本文没有执行固件构建、烧录或接线实验。


[上一章](P059_驱动示例总目录.md) · [返回大纲](大纲.md) · [下一章](P061_以太网示例目录.md)
