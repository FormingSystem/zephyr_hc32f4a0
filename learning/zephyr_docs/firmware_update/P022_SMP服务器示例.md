---
id: learning.zephyr-docs.firmware_update.mgmtex-smp-svr
title: SMP服务器示例
kind: reference
status: maintained
domains: [zephyr, firmware_update]
source_url: https://docs.zephyrproject.org/latest/samples/subsys/mgmt/mcumgr/smp_svr/README.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

<a id="smp-svr"></a>

# 第22章\_SMP服务器示例

原文：[SMP server](https://docs.zephyrproject.org/latest/samples/subsys/mgmt/mcumgr/smp_svr/README.html)。读取日期：2026-10-13，`latest`。

## 22.1\_服务器能力与前提

示例 `smp_svr` 实现 **简单管理协议（Simple Management Protocol，SMP）**服务器，使用MCUmgr管理协议的编码与传输机制。基础说明见[设备管理概览](P001_设备管理概览.md)。

原页列出的默认传输为 **命令解释器（Shell）**、蓝牙（Bluetooth）和 **用户数据报协议（User Datagram Protocol，UDP）**。管理组包括文件系统 `fs_mgmt`、镜像 `img_mgmt`、操作系统 `os_mgmt`、统计 `stat_mgmt` 和Shell命令 `shell_mgmt`。下方不同配置片段决定实际编入的组合，不能把列表理解为所有板卡默认同时可用。

镜像管理要求MCUboot **引导加载程序（Bootloader）**，参见[设备固件升级](P002_设备固件升级.md)。远端交互需要一个MCUmgr客户端工具，选择入口见[MCUmgr设备管理](P006_MCUmgr设备管理.md)。

仅Linux用户：若要用 **蓝牙低功耗（Bluetooth Low Energy，BLE）**测试空中升级，但没有内置或可插拔无线控制器，可以按[使用BlueZ连接控制器](../bluetooth_samples/P016_HCI_UART传输.md#bluetooth-hci-uart-bluez)构建并连接控制器。

## 22.2\_蓝牙与串口构建

以下原命令从Zephyr源码目录使用west和 **系统构建（System Build，sysbuild）**同时构建MCUboot与应用。板卡名称是官方示例目标，不意味着HC32已经具有相同外设和分区配置。应用目录为 `samples/subsys/mgmt/mcumgr/smp_svr`。

蓝牙配置：

```shell
west build -b nrf52dk/nrf52832 --sysbuild samples/subsys/mgmt/mcumgr/smp_svr -- -DEXTRA_CONF_FILE="bt.conf"
```

串口配置，并启用文件系统和Shell管理：

```shell
west build -b frdm_k64f --sysbuild samples/subsys/mgmt/mcumgr/smp_svr -- -DEXTRA_CONF_FILE="serial.conf;fs.conf;shell-mgmt.conf"
```

**原始通用异步收发器传输（Raw Universal Asynchronous Receiver/Transmitter，Raw UART）**直接发送MCUmgr二进制包，不使用控制台编码；因此同一UART不能同时供Shell等文本业务使用。原始串口加文件系统配置：

```shell
west build -b nrf52840dk/nrf52840 --sysbuild samples/subsys/mgmt/mcumgr/smp_svr -- -DEXTRA_CONF_FILE="raw-serial.conf;fs.conf"
```

## 22.3\_USB与Shell构建

**通用串行总线（Universal Serial Bus，USB）**的 **通信设备类（Communications Device Class，CDC）**配合 **抽象控制模型（Abstract Control Model，ACM）**提供CDC ACM虚拟串口后端；CMake参数 `-DEXTRA_DTC_OVERLAY_FILE` 指定额外设备树覆盖文件：

```shell
west build -b nrf52840dk/nrf52840 --sysbuild samples/subsys/mgmt/mcumgr/smp_svr -- -DEXTRA_CONF_FILE="cdc.conf" -DEXTRA_DTC_OVERLAY_FILE="usb.overlay"
```

测试该配置时，应连接板上直接接到 **微控制器（Microcontroller Unit，MCU）**的USB端口。

Shell传输配置：

```shell
west build -b frdm_k64f --sysbuild samples/subsys/mgmt/mcumgr/smp_svr -- -DEXTRA_CONF_FILE="shell.conf"
```

## 22.4\_UDP构建

示例同时启用 **互联网协议第4版（Internet Protocol version 4，IPv4）**与第6版IPv6，也可分别启用或禁用。普通UDP配置：

```shell
west build -b frdm_k64f --sysbuild samples/subsys/mgmt/mcumgr/smp_svr -- -DEXTRA_CONF_FILE="udp.conf"
```

802.15.4 Sub-GHz（低于1 GHz频段）网络配置：

```shell
west build -b beagleconnect_freedom --sysbuild samples/subsys/mgmt/mcumgr/smp_svr -- -DEXTRA_CONF_FILE="overlay-udp.conf;802154-subg.conf"
```

**数据报传输层安全（Datagram Transport Layer Security，DTLS）**配置：

```shell
west build -b bl5340_dvk/nrf5340/cpuapp --sysbuild samples/subsys/mgmt/mcumgr/smp_svr -- -DEXTRA_CONF_FILE="udp-dtls.conf"
```

> 译注：原文这一分支使用 `overlay-udp.conf`，其他分支使用 `udp.conf`。本地版本仅有 `udp.conf` 而无 `overlay-udp.conf`；采用该版本时应使用存在的片段，并核对其配置内容。

## 22.5\_烧录与回显

初始应用构建到主槽slot-0，分区背景见[闪存映射官方说明](https://docs.zephyrproject.org/latest/services/storage/flash_map/flash_map.html#flash-map-api)。同时烧录MCUboot和应用：

```shell
west flash
```

复位开发板后，使用选定客户端的echo（回显）功能发送字符串，目标设备将其返回。

带 **板载J-Link（J-Link On-Board，J-Link OB）**的板卡，若调试器同时启用CDC和 **大容量存储类（Mass Storage Class，MSC）**，其虚拟 **大容量存储设备（Mass Storage Device，MSD）**拖放下载功能可能因J-Link固件USB端点配置而限制最大包大小，导致CDC UART上的管理命令失败；镜像上传时尤其明显，Nordic nRF52840 DK是原文示例。可按[禁用MSD功能](../debugging/P005_Nordic_Segger_JLink.md#nordic-segger-msd)处理。

## 22.6\_固件升级流程与槽映射

能与SMP服务器通信后，可测试 **空中设备固件升级（Over-The-Air Device Firmware Upgrade，OTA DFU）**，蓝牙和UDP均可承载。一般过程为：

1. 用sysbuild构建启用MCUboot的应用。
2. 通过MCUmgr客户端上传签名镜像。
3. 列出设备上的镜像。
4. 将上传镜像标记为测试。
5. 经客户端远程复位设备。
6. 根据需要经客户端确认上传镜像；不确认则测试启动不变为永久。

原文说明直接上传支持四个目标镜像，前两个对应主槽和次槽，并给出下表。表头DTS指 **设备树源码（Devicetree Source）**：

| 原文DTS标签列 | 槽 | 工具参数 `-n <image>` |
| --- | --- | --- |
| `image-0` | slot-0 | 1 |
| `image-1` | slot-1 | 0、1 |
| `image-2` | 原表未填写 | 2 |
| `image-3` | 原表未填写 | 3 |

> 译注：原表称“DTS标签”，这里列出的实际是常见分区名称，且其上传编号随直接上传配置和实现而异，不能直接等同于逻辑镜像内的0/1槽号。应先使用[槽信息命令](P012_镜像管理组.md)查询实际 `upload_image_id`，再确定目标，不从这张历史表推断当前固件分区。

## 22.7\_上传、列表与测试

按所选工具文档选择新的签名固件文件并上传。上传开始时设备可能先擦除镜像槽，某些目标要等待数十秒。

随后列出slot-0和slot-1中存在的镜像，检查状态和摘要。要让MCUboot切换镜像，先按工具说明将新镜像标记为测试，重启后切换运行。

某些工具无需上传就能读取镜像摘要。imgtool命令 `dumpinfo` 也可从签名更新文件中读取，不过输出采用C十六进制数组形式。下面保留原命令及输出；路径相对于包含 `smp_svr/zephyr/` 的构建目录：

输出中的 **类型—长度—值（Type-Length-Value，TLV）**区的 **256位安全散列算法（Secure Hash Algorithm 256-bit，SHA-256）**名称在原日志中写作 `SHA256`。

```text
imgtool dumpinfo smp_svr/zephyr/zephyr.signed.bin

Printing content of signed image: zephyr.signed.bin

#### Image header (offset: 0x0) ############################
magic:              0x96f3b83d
...
#### TLV area (offset: 0xbfa0) #############################
magic:     0x6907
area size: 0x150
        ---------------------------------------------
        type: SHA256 (0x10)
        len:  0x20
        data: 0x9b 0xa9 0x84 0x48 0xe5 0x4d 0xac 0x40
              0x62 0x29 0xe2 0x11 0x17 0x96 0x66 0xd9
              0xae 0x83 0x9a 0x37 0x71 0x00 0xfc 0xe2
              0xc0 0x30 0x30 0x4f 0xfc 0x40 0x58 0xaa
        ---------------------------------------------
...
```

其中的摘要合并为 `9ba98448e54dac406229e211179666d9ae839a377100fce2c030304ffc4058aa`。这是镜像验证摘要，不要与整文件上传会话摘要混淆，见[镜像管理组](P012_镜像管理组.md)。

## 22.8\_复位、确认与文件传输

按工具说明远程复位，并从控制台观察MCUboot交换slot-0与slot-1。新镜像此时运行于slot-0；未确认时，下次复位会将其退回slot-1。用所选工具确认镜像后才保留新应用。该过程对应支持交换与回退的引导模式。

**原文注意：**如果上传的就是slot-0中已经运行的同一个镜像，两槽摘要相同，该流程不会按预期完成。

SMP服务器还支持设备 **文件系统（File System）**的上传/下载，例如从非易失性存储读取文件日志。使用sysbuild构建和烧录后，经客户端执行文件传输；必须知道并使用设备上文件的完整路径。这里指设备路径，不是开发主机地址。

[上一章：管理示例入口](P021_管理示例入口.md) · [下一章：HTTP固件升级示例](P023_HTTP固件升级示例.md) · [返回大纲](大纲.md)
