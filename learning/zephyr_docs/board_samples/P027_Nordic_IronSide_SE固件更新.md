---
id: learning.zephyr-docs.board-samples.page-27
title: Nordic_IronSide_SE固件更新
kind: reference
status: maintained
domains: [zephyr, boards, samples]
source_url: https://docs.zephyrproject.org/latest/samples/boards/nordic/nrf_ironside/update/README.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

<a id="nrf_ironside_update"></a>

# 第27章\_Nordic IronSide SE 固件更新（Nordic IronSide SE firmware update）

原文：[官方页面](https://docs.zephyrproject.org/latest/samples/boards/nordic/nrf_ironside/update/README.html)。快照读取日期：2026-10-15；来源摘要见[来源记录](../SOURCES.md)。

[在 GitHub 浏览源码（Browse source code on GitHub）](https://github.com/zephyrproject-rtos/zephyr/blob/main//samples/boards/nordic/nrf_ironside/update/README.rst/..)

<a id="overview"></a>

## 27.1 概述（Overview）

Nordic IronSide SE 更新示例在已安装 IronSide SE 的 SoC 上更新 IronSide SE 固件。通过 IronSide SE 固件发布 ZIP 文件，可以更新其主镜像（Main image）与恢复镜像（Recovery image）。

<a id="update-procedure"></a>

## 27.2 更新流程（Update procedure）

更新流程如下：

1. 应用调用 IronSide SE 更新服务，传入与 IronSide SE 固件更新 HEX 文件位置相对应的参数。

2. 应用打印服务调用的返回值，并输出更新 HEX 文件中的信息。

3. 服务调用完成后，IronSide SE 固件会更新设备内部状态。

4. 固件在设备下一次启动时安装更新；此操作可能耗时数秒。

操作完成后，可以读取启动报告（Boot report），确认更新已发生。

<a id="building-and-running-the-application-for-nrf54h20dk-nrf54h20-cpuapp"></a>

## 27.3 为 nrf54h20dk/nrf54h20/cpuapp 构建并运行应用

注意（Note）

只有设备上已经安装某个版本的 IronSide SE，才能使用本应用。

> 译注——更新与首次安装：本应用调用已有 IronSide SE 提供的更新服务，不能用于替代首次安装。CONFIG_UPDATE_BLOB_ADDRESS 指向设备地址空间中的更新数据，默认值配合官方发布包；它不是电脑文件路径。主镜像与恢复镜像的 HEX 命令是二选一分支。

1. 解压 IronSide SE 发布 ZIP，取得更新 HEX 文件：

> 译注——文件来源与位置：ZIP 由官方固件发布提供，解压产生 update/ 下的 HEX。unzip 和以 update/ 开头的 nrfutil program 命令在读者选择的发布包目录执行；west 命令则回到所用 Zephyr 源码根。使用 UCRT64 Bash 或 Linux Bash，先准备 west、工具链及带所需 device 命令的 nrfutil，并确认实际连接的目标板。各步失败时先处理对应错误，不继续复位或把服务返回成功当作更新已经安装。

```text
unzip nrf54h20_soc_binaries_v.*.zip
```

2. 使用下面两条命令中的一条（不要同时使用两条），烧写发布 ZIP 中相应的更新 HEX 文件：

**分支 A：更新 IronSide SE 固件：**

```text
nrfutil device program --traits jlink --firmware update/ironside_se_update.hex
```

**分支 B：更新 IronSide SE 恢复固件：**

```text
nrfutil device program --traits jlink --firmware update/ironside_se_recovery_update.hex
```

3. 构建并烧写应用：

```text
# From the root of the zephyr repository
west build -b nrf54h20dk/nrf54h20/cpuapp samples/boards/nordic/nrf_ironside/update
west flash
```

4. 触发复位：

```text
nrfutil device reset --reset-kind RESET_PIN --traits jlink
```

5. 检查启动报告，确认已安装新版本：

> 译注——完成判断：服务接受请求、复位安装和读取启动报告是不同阶段。对照更新前后报告中的主镜像／恢复镜像版本与 update status，确认所选镜像确已更新。本次只翻译和核对流程，没有向设备写入固件。

```text
nrfutil device x-ironside-boot-report-read --traits jlink
```

> 译注——实现入口：[samples/boards/nordic/nrf_ironside/update/src/main.c](../../../samples/boards/nordic/nrf_ironside/update/src/main.c)与[samples/boards/nordic/nrf_ironside/update/prj.conf](../../../samples/boards/nordic/nrf_ironside/update/prj.conf)。仓库源码仅作参照，版本可能与本次官方页面不同；本地链接按文档位置相对解析。

对应官方文档源码：[samples/boards/nordic/nrf_ironside/update/README.rst](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/boards/nordic/nrf_ironside/update/README.rst)。

> 译注——源码跟踪：本仓库[对应源码](../../../samples/boards/nordic/nrf_ironside/update/README.rst)可用于对照，版本可能与网页不同。本批仅翻译和核对文档，未构建、烧录或执行硬件实验。

[上一章](P026_蓝牙活动期间写入Nordic闪存.md) · [返回大纲](大纲.md) · [下一章](P028_Nordic_LED矩阵.md)
