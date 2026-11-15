---
id: learning.zephyr-docs.networking.page-121
title: gPTP示例
kind: reference
status: maintained
domains: [zephyr, networking, development]
source_url: https://docs.zephyrproject.org/latest/samples/net/ethernet/gptp/README.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第121章\_gPTP示例

原文：[官方页面](https://docs.zephyrproject.org/latest/samples/net/ethernet/gptp/README.html)。读取日期：2026-10-14；保存的 latest 页面及 HTML 摘要见[来源记录](../SOURCES.md)。

## 1. 概述（Overview）

Zephyr 的通用精确时间协议（generic Precision Time Protocol，gPTP）示例启用 gPTP，注册相位不连续（Phase Discontinuity）回调，启用流量类别支持，即发送多队列（TX Multi Queues），并在启用 VLAN 时完成 VLAN 设置。网络命令行（net-shell）也会启用，便于监测 gPTP 功能。

源码位于 [`samples/net/ethernet/gptp`](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/net/ethernet/gptp)，可[在 GitHub 查看官方源码](https://github.com/zephyrproject-rtos/zephyr/blob/main//samples/net/ethernet/gptp/README.rst/..)。

## 2. 前提条件（Requirements）

用于调试的通用主机连接方法见[native_sim 板联网](P008_native_sim联网.md#networking-with-native-sim)。

## 3. 构建和运行（Building and Running）

可以按照上述联网文档，在 `native_sim` 板中运行应用，也可以使用 NXP FRDM-K64F、Nucleo-H743-ZI、Nucleo-H745ZI-Q、Nucleo-F767ZI 或 Atmel SAM-E70 Xplained 等嵌入式设备。

注意：gPTP 仅支持具有以太网端口、且能够采集已发送和已接收以太网帧时间戳的开发板。

从已准备好工具链和依赖的 Zephyr 源码根目录构建示例，将原文占位符 `<board to use>` 替换为实际目标：

```sh
west build -b <board to use> samples/net/ethernet/gptp
```

运行后，在设备的网络命令行执行 `net gptp` 可查看一般 gPTP 信息。对于端口 1，`net gptp 1` 可输出其统计等详细信息。执行命令行命令可能影响 gPTP 数据包收发时序，使最高主时钟（Grandmaster）把设备标记为不具备 AS 能力（Non AS Capable）并将其禁用。

## 4. 设置 Linux 主机（Setting up Linux Host）

如果需要 VLAN，官方 [`samples/net/ethernet/vlan/vlan-setup-linux.sh`](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/net/ethernet/vlan/vlan-setup-linux.sh) 可以在 Linux 主机创建两个 VLAN 及通往 Zephyr 的路由。使用 `native_sim` 时，`net-setup.sh` 也可以通过下列命令自动设置 VLAN：

```sh
./net-setup.sh -c zeth-vlan.conf
```

> 译注——执行位置：主机侧命令使用 Linux Bash。上面的脚本来自官方外部 `net-tools`，在包含脚本和配置的工具目录执行；该目录的获取和网络准备见前面的主机联网文档。脚本创建的是主机网络配置，并不编译应用。

### 4.1 使用 OpenAVnu gPTP（Hardware Timestamping）

[OpenAVnu 项目](https://github.com/AVnu)提供可在 Linux 主机运行的 gPTP 守护进程，它能够充当 IEEE 802.1AS 网络的最高主时钟。OpenAVnu 不能与 `native_sim` 配合使用：`native_sim` 只有软件时间戳，而 OpenAVnu 只支持硬件时间戳（Hardware Timestamping）。与 `native_sim` 配合的方法见后面的 linuxptp 小节。

> 译注——原文笔误：此处原文写作 `IEEE 801.1AS`，结合本页协议名称和对应标准，应为 `IEEE 802.1AS`。

在 Linux Bash 中进入准备存放外部项目的实际目录，然后获取 OpenAvnu/gPTP 源码：

```sh
git clone git@github.com:AVnu/gptp.git
```

> 译注——下载前提：这是原文保留的 GitHub SSH 克隆地址，使用者需要自己的 GitHub SSH 访问配置。外部源码应按读者的工作区位置放置，不依赖作者的目录。

下载后，进入克隆所得的 `gptp` 源码目录，在 Linux 中编译：

```sh
mkdir build
cd build
cmake ..
make
cp ../gptp_cfg.ini .
```

> 译注——目录与产物：`build` 是这里自行创建的外部 gPTP 构建目录。`cmake ..`、`make` 和复制配置文件在该目录执行；需要主机已安装该项目要求的编译工具和依赖。后续 `./gptp` 指向这里生成的可执行文件。

编辑复制后的 `gptp_cfg.ini`，将 `neighborPropDelayThresh` 设为 `10000`。原文说明，在 FRDM-K64F 上运行 gPTP 时，默认值 `800` 太小。随后指定正确网络接口和配置文件启动守护进程：

```sh
sudo ./gptp enp0s25 -F gptp_cfg.ini
```

示例中的 `enp0s25` 是连接 Zephyr 设备的主机网口名称，应换成实际接口。配置正确时，gPTP 会出现类似以下日志：

```text
INFO     : GPTP [13:01:14:837] gPTP starting
INFO     : GPTP [13:01:14:838] priority1 = 248
INFO     : GPTP [13:01:14:838] announceReceiptTimeout: 3
INFO     : GPTP [13:01:14:838] syncReceiptTimeout: 3
INFO     : GPTP [13:01:14:838] LINKSPEED_100MB - PHY delay
                    TX: 1044 | RX: 2133
INFO     : GPTP [13:01:14:838] LINKSPEED_1G - PHY delay
                    TX: 184 | RX: 382
INFO     : GPTP [13:01:14:838] neighborPropDelayThresh: 10000
INFO     : GPTP [13:01:14:838] syncReceiptThreshold: 8
ERROR    : GPTP [13:01:14:838] Using clock device: /dev/ptp0
STATUS   : GPTP [13:01:14:838] Starting PDelay
STATUS   : GPTP [13:01:14:838] Link Speed: 1000000 kb/sec
STATUS   : GPTP [13:01:14:871] AsCapable: Enabled
STATUS   : GPTP [13:01:16:497] New Grandmaster "3C:97:0E:FF:FE:23:F2:32" (previous "00:00:00:00:00:00:00:00")
STATUS   : GPTP [13:01:16:497] Switching to Master
```

若 Zephyr 正常与 gPTP 守护进程同步，还会打印：

```text
STATUS   : GPTP [13:01:25:965] AsCapable: Enabled
```

> 译注——日志含义：日志依次展示配置参数、PHY 收发延迟、时钟设备、对等时延测量启动、AS 能力启用、新最高主时钟以及切换到主时钟状态。`/dev/ptp0` 是原日志中的 Linux PTP 设备节点，不是作者仓库路径；设备编号由实际主机决定。上面的日志是官方示例输出，不是本次实测结果。

默认情况下，Zephyr 的 gPTP 不向控制台打印调试信息。可以在配置文件中启用 [`CONFIG_NET_GPTP_LOG_LEVEL_DBG`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_GPTP_LOG_LEVEL_DBG)。

### 4.2 使用 linuxptp（Software Timestamping）

`native_sim` 应使用支持软件时间戳（Software Timestamping）的 linuxptp 项目。

从选定的外部项目存放目录获取源码：

```sh
git clone git://git.code.sf.net/p/linuxptp/code
```

编译 ptp4l 守护进程，并按下列方式启动：

```sh
sudo ./ptp4l -2 -f gPTP-zephyr.cfg -i zeth -m -q -l 6 -S
```

以 `default.cfg` 为基础，将它复制为 `gPTP-zephyr.cfg`，再按实际需要修改。

> 译注——操作顺序：原页面没有给出 ptp4l 的编译命令，也没有给出完整的 `gPTP-zephyr.cfg` 内容。应先按照外部 linuxptp 项目的构建说明生成 `ptp4l`，准备配置文件，再从包含该可执行文件和配置文件的目录执行启动命令。这里的 `zeth` 是示例接口名；`-S` 选择软件时间戳。配置文件必须在执行 `-f gPTP-zephyr.cfg` 之前已存在，不能仅克隆源码就认为守护进程已安装或同步成功。

## 5. 多端口设置（Multiport Setup）

将 [`CONFIG_NET_GPTP_NUM_PORTS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_GPTP_NUM_PORTS) 设为大于 `1` 时，gPTP 示例创建多个时间敏感网络（Time-Sensitive Networking，TSN）端口。原文说明，目前这种配置仅支持 `native_sim`。设备树中 `zephyr,native-tap` 接口的数量必须与 [`CONFIG_NET_GPTP_NUM_PORTS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_GPTP_NUM_PORTS) 相同。

配置两个端口时，使用 `overlay-multiport.conf` 和 `overlay-multiport.overlay` 构建，后者添加第二个 TAP 接口。从 Zephyr 源码根目录执行：

```sh
west build -b native_sim samples/net/ethernet/gptp -- -DEXTRA_CONF_FILE=overlay-multiport.conf -DEXTRA_DTC_OVERLAY_FILE=overlay-multiport.overlay
```

还需在 `net-tools` 中启用这些端口。两个端口时，在 Linux 主机的 `net-tools` 目录执行以下命令创建对应接口：

```sh
sudo ./net-setup.sh -c zeth0-gptp.conf -i zeth0 start
sudo ./net-setup.sh -c zeth1-gptp.conf -i zeth1 start
```

然后为两个接口分别启动 ptp4l。需要使用两个终端；`native_sim` 只有软件时钟，不能使用 OpenAVnu：

```sh
cd <ptp4l directory>
sudo ./ptp4l -2 -f gPTP-zephyr.cfg -m -q -l 6 -S -i zeth0
sudo ./ptp4l -2 -f gPTP-zephyr.cfg -m -q -l 6 -S -i zeth1
```

> 译注——两个终端：`<ptp4l directory>` 是读者实际编译 ptp4l 的目录占位符。两个终端都要先进入该目录，并能读取 `gPTP-zephyr.cfg`；一个运行 `-i zeth0`，另一个运行 `-i zeth1`。第一条守护进程命令占用前台时，不能期待同一终端紧接着执行第二条。

原文随后给出编译 Zephyr 应用的命令：

```sh
west build -b native_sim samples/net/ethernet/gptp
```

> 译注——多端口配置一致性：这一后续命令省略了前面的两个 overlay 参数。如果重新配置到全新构建目录，只靠它不会建立相同的双端口设置。要复现本节，应沿用带两个 overlay 的构建命令和产物。官方 [overlay-multiport.conf](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/net/ethernet/gptp/overlay-multiport.conf) 设置两个 gPTP 端口，[overlay-multiport.overlay](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/net/ethernet/gptp/overlay-multiport.overlay) 把两个 TAP 对应到 `zeth0`、`zeth1`。这些配置文件由官方示例随附。

镜像构建完成后，从该 Zephyr 源码根目录启动：

```sh
build/zephyr/zephyr.exe -attach_uart
```

> 译注——验证范围：这里运行的是 Linux 主机上的 `native_sim` 程序；不能因文件扩展名为 `.exe` 就把它当成 Windows 原生程序。启动后结合 `net gptp`、端口状态及主机 ptp4l 日志判断连接；软件时钟测试不证明硬件时间戳精度，也不替代协议栈总览中尚未完成的多端口验证。

## 6. 静态时间接收端设置（Static timeReceiver Setup）

采用 IEEE 802.1AS 车载配置规范的网络中，网桥发送 Sync 和 Follow_Up，不发送 Announce，因此默认协议栈不会选出时间接收端口。构建时加入 [`samples/net/ethernet/gptp/overlay-static-time-receiver.conf`](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/net/ethernet/gptp/overlay-static-time-receiver.conf)，可以把端口固定为时间接收端角色：

```sh
west build -b <board to use> samples/net/ethernet/gptp -- -DCONF_FILE="prj.conf overlay-static-time-receiver.conf"
```

该命令从 Zephyr 源码根目录执行，板目标占位符仍需替换。配置文件是官方随附文件，启用 [`CONFIG_NET_GPTP_STATIC_TIME_RECEIVER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_GPTP_STATIC_TIME_RECEIVER)。

可以让 linuxptp 的 ptp4l 作为不发送 Announce 的最高主时钟来测试，例如使用基于 linuxptp 随附 `automotive-master.cfg` 的配置。

## 7. 另请参阅（See Also）

- [gPTP 支持接口](https://docs.zephyrproject.org/latest/doxygen/html/group__gptp.html)。
- [精确时间协议时间表示（PTP Time）](https://docs.zephyrproject.org/latest/doxygen/html/group__ptp__time.html)。


<a id="gptp"></a>
<a id="overview"></a>
<a id="requirements"></a>
<a id="building-and-running"></a>
<a id="setting-up-linux-host"></a>
<a id="multiport-setup"></a>
<a id="static-timereceiver-setup"></a>
<a id="see-also"></a>

[上一章](P120_LLDP示例.md) · [返回大纲](大纲.md) · [下一章](P122_以太网服务质量示例.md)
