---
id: learning.zephyr-docs.interaction.page-11
title: 文件系统Shell示例
kind: reference
status: maintained
domains: [zephyr, shell, input]
source_url: https://docs.zephyrproject.org/latest/samples/subsys/shell/fs/README.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第11章\_文件系统Shell示例

原文：[官方页面](https://docs.zephyrproject.org/latest/samples/subsys/shell/fs/README.html)。读取日期：2026-10-14；保存的 latest 页面及 HTML 摘要见[来源记录](../SOURCES.md)。

## 11.1\_概述与要求

本示例通过 Shell 访问闪存（Flash）中的 LittleFS 文件系统分区。开发板需要支持 LittleFS，并提供 UART 控制台。

## 11.2\_构建

### native_sim

可以这样为 [native_sim](../native_reference/P004_Native_Simulator本机模拟器.md#native_sim) 构建示例。主机终端位于 Zephyr 源码根目录，工具链、模块及 native_sim 主机依赖已准备好：

```sh
west build -b native_sim samples/subsys/shell/fs
```

默认使用闪存模拟器（Flash Simulator），在当前目录用 `flash.bin` 文件保存闪存内容。可用以下命令查看控制其行为的选项：

```sh
zephyr/zephyr.exe -help
```

译注：上一条原始可执行路径相对于构建目录，应在构建产物所在目录运行；采用默认 `build` 目录时，从源码根应定位到 `build/zephyr/zephyr.exe`。这不同于要求仓库位于某个固定盘符。

如何连接 UART，参阅 [native_sim的UART说明](../native_reference/P004_Native_Simulator本机模拟器.md#native-ptty-uart)。

### 通过FUSE从主机文件系统访问

启用 [主机FUSE文件系统访问](../native_reference/P004_Native_Simulator本机模拟器.md#native-fuse-flash) 后，闪存文件系统也会挂载到 Linux 主机，可从主机文件系统访问。FUSE 为用户空间文件系统（Filesystem in Userspace）。

开始构建前，确保搜索路径包含 i386 的 pkg-config 目录，并安装 32 位 `libfuse`。要求的背景见 [native_sim说明](../native_reference/P004_Native_Simulator本机模拟器.md#native-fuse-flash)。以下是原文的 Linux 主机配置与构建命令：

```sh
export PKG_CONFIG_PATH=/usr/lib/i386-linux-gnu/pkgconfig
```

```sh
west build -b native_sim samples/subsys/shell/fs -- -DCONFIG_FUSE_FS_ACCESS=y
```

译注：`/usr/lib/i386-linux-gnu/pkgconfig` 是原文所用 Linux 系统的库搜索位置，不是作者仓库绝对路径；是否使用该目录需与目标架构和已安装软件包匹配。

### Reel Board

```sh
west build -b reel_board samples/subsys/shell/fs
```

### Particle Xenon

该目标进行了定制，使用与 [LittleFS文件系统示例](../storage/P085_LittleFS文件系统示例.md) 相同的 SPI NOR 分区表（Partition Table）。

```sh
west build -b particle_xenon samples/subsys/shell/fs
```

### Flash加载

要使用 `flash load`，按原文选择 `prj_flash_load.conf` 构建。该配置使用较大的接收（RX）缓冲区；缓冲区过小时，传输大文件可能丢失数据。

## 11.3\_运行与加载文件系统

开发板启动后会出现 Shell 提示符。文件系统命令均位于 `fs` 子命令下，先挂载（Mount）LittleFS：

```sh
fs mount littlefs /lfs
```

以下命令在设备的 Zephyr Shell 中输入，用于把主机文件系统镜像加载到闪存：

```text
flash load <address> <size>
```

它通过 UART 接收数据，直接写入指定闪存地址。数据须按目标闪存要求对齐（Alignment）；否则会报错，不加载数据。

主机端使用 `dd`，并指定 `bs=64`。原文指出，若每块大于 64 字节，数据可能丢失，Zephyr Shell 无法收到全部内容。

设备控制台示例：

```text
flash load 0x7a000 0x5000
```

Linux 主机终端示例：

```sh
dd if=filesystem of=/dev/ttyACM0 bs=64
```

传输期间会显示已写入的数据块数量，成功结束后显示 `Read all`（已读取全部数据）。

译注：`0x7a000`、`0x5000` 是原示例的设备地址和大小，必须与目标分区及镜像一致；它们不是可移植的存储布局。`filesystem` 为待传镜像，`/dev/ttyACM0` 为原文串口设备节点。上述主机原始字节传输不同于下一章 `devmem load` 的十六进制文本输入，不能混用。

## 11.4\_文件系统Shell命令

### Mount：挂载

把文件系统分区挂载到指定挂载点：

```text
fs mount (littlefs|fat) <path>
```

### Ls：列目录

列出指定路径中的文件和目录：

```text
fs ls [path]
```

### Cd：切换目录

把当前工作目录切换到指定路径：

```text
fs cd [path]
```

### Pwd：显示目录

显示当前工作目录：

```text
fs pwd
```

### Write：写文件

向指定文件写入十六进制数，可选地指定文件内偏移（Offset）：

```text
fs write <path> [-o <offset>] <hex number> ...
```

### Read：读文件

读取文件，以十六进制和 ASCII 格式转储：

```text
fs read <path>
```

### Trunc：截断

截断指定文件：

```text
fs trunc <path>
```

### Mkdir：创建目录

```text
fs mkdir <path>
```

### Rm：删除

删除文件或目录：

```text
fs rm <path>
```

## 11.5\_从主机访问闪存

对于 [native_sim开发板](../native_reference/P004_Native_Simulator本机模拟器.md#native_sim)，Linux 主机可以访问闪存分区；默认入口是相对于开始构建所在目录的 `flash` 目录。

译注：本段承接前面的 FUSE 主机访问功能，不能把只有闪存模拟器生成 `flash.bin` 理解为已经挂载主机文件系统。实际入口随运行配置与工作目录确定。

参阅：[文件系统API](../storage/P033_文件系统接口.md)。


译注核对来源：[samples/subsys/shell/fs/src/main.c](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/subsys/shell/fs/src/main.c)、[samples/subsys/shell/fs/prj_flash_load.conf](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/subsys/shell/fs/prj_flash_load.conf)、[subsys/fs/shell.c](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/fs/shell.c)。

本仓库的[对应示例源码](../../../samples/subsys/shell/fs/src/main.c)可用于跟踪，版本可能与网页不同；本批仅翻译和核对文档，没有执行构建、写内存／闪存或硬件操作。

<a id="shell-fs"></a>
<a id="overview"></a>
<a id="requirements"></a>
<a id="building"></a>
<a id="native-sim"></a>
<a id="with-fuse-access-in-the-host-filesystem"></a>
<a id="reel-board"></a>
<a id="particle-xenon"></a>
<a id="flash-load"></a>
<a id="running"></a>
<a id="loading-filesystem-from-host-pc-to-flash-memory"></a>
<a id="files-system-shell-commands"></a>
<a id="mount"></a>
<a id="ls"></a>
<a id="cd"></a>
<a id="pwd"></a>
<a id="write"></a>
<a id="read"></a>
<a id="trunc"></a>
<a id="mkdir"></a>
<a id="rm"></a>
<a id="flash-host-access"></a>
<a id="see-also"></a>

[上一章](P010_Shell命令模块示例.md) · [返回大纲](大纲.md) · [下一章](P012_内存加载Shell示例.md)
