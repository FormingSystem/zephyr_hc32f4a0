---
id: learning.zephyr-docs.tfm.page-10
title: TFM固件更新示例
kind: reference
status: maintained
domains: [zephyr, tfm, security]
source_url: https://docs.zephyrproject.org/latest/samples/tfm_integration/tfm_fwu/README.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第10章\_TFM固件更新示例

原文：[官方页面](https://docs.zephyrproject.org/latest/samples/tfm_integration/tfm_fwu/README.html)。读取日期：2026-10-14；保存的 latest 页面及 HTML 摘要见[来源记录](../SOURCES.md)。

## 10.1\_概述（Overview）

本 TF-M 集成示例展示如何通过 PSA 固件更新 API（PSA Firmware Update API，PSA FWU API）更新设备固件；TF-M 运行在安全侧，Zephyr 运行在非安全侧。

示例包含两个应用：

- 主应用（Main Application）：通过 PSA FWU API 把新固件写入更新分区，然后请求重新启动以应用更新。
- 替换应用（Swapped Application）：更新成功后启动的新固件镜像。

为简化流程，替换应用的签名镜像在构建时直接嵌入主应用二进制文件。

> 原文注意：镜像签名、加密及防回滚（Anti-Rollback）由 TF-M 配置选项控制。本示例使用 TF-M 自带的默认开发密钥；用于生产时，应换成自己的密钥，并确认配置符合产品安全要求。

## 10.2\_构建与运行（Building and Running）

本示例要求使用系统构建（System Build，sysbuild），并在支持 TF-M 的平台运行。原文从 Zephyr 仓库根目录执行的命令为：

```sh
# From the root of the zephyr repository
west build -b mps2/an521/cpu0/ns samples/tfm_integration/tfm_fwu
```

译注——sysbuild 入口：原页上述命令没有显式给出 `--sysbuild`。当前官方 `tests.yaml` 明确设置 `sysbuild: true`，`sysbuild.cmake` 负责加入并先构建 `swapped_app`；主应用的 CMake 再读取它的已签名镜像生成嵌入文件。因此，在没有通过 west 配置默认启用 sysbuild 的工作区，应显式选择它。以下为基于当前源码补充的调用方式，不是原文代码块：

```sh
west build --sysbuild -b mps2/an521/cpu0/ns samples/tfm_integration/tfm_fwu
```

该命令以已准备好工具链、TF-M 模块及依赖为前提；源码根目录由读者工作区决定。若配置阶段未建立 `swapped_app`，先核对 sysbuild 入口，不能用手工复制旧镜像掩盖构建依赖缺失。

译注——镜像关系：`sysbuild.conf` 选择 `SB_CONFIG_BOOTLOADER_NONE=y`，原因是 TF-M 已提供自己的 BL2，不应再由 sysbuild 构建另一份 MCUboot。主应用根据加密选项嵌入 `zephyr_ns_signed.bin` 或 `zephyr_ns_signed_encrypted.bin`。这演示本地固件更新流程，并不包含网络下载服务。

## 10.3\_示例输出（Sample Output）

主应用输出如下：

```text
TF-M FWU on mps2
Installing new firmware for component 1
Starting FWU
Writing 17286 bytes
Finishing FWU
Installing FWU
FWU installed, reboot required
Rebooting to apply the new firmware...
```

日志表示为组件 1 安装新固件，依次开始更新、写入数据、结束写入和安装，然后请求重启。

重启后，替换应用输出：

```text
Swapped application booted on mps2
FWU completed successfully
```

译注——源码跟踪：当前主应用先要求组件处于 `PSA_FWU_READY`，按 `PSA_FWU_MAX_WRITE_SIZE` 分块写入；安装返回需要重启的状态后调用 `psa_fwu_request_reboot()`。替换应用会查询状态，在试运行（Trial）状态下调用 `psa_fwu_accept()`，完成后清理更新状态并确认回到 READY。源码注释要求实际产品在接受更新前做自身功能检查；示例没有实现这些产品检查。上述字节数与短日志来自原页，不是当前版本完整输出，也不是本次实测结果。


译注核对来源：[samples/tfm_integration/tfm_fwu/src/main.c](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/tfm_integration/tfm_fwu/src/main.c)、[samples/tfm_integration/tfm_fwu/prj.conf](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/tfm_integration/tfm_fwu/prj.conf)、[samples/tfm_integration/tfm_fwu/CMakeLists.txt](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/tfm_integration/tfm_fwu/CMakeLists.txt)、[samples/tfm_integration/tfm_fwu/sysbuild.cmake](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/tfm_integration/tfm_fwu/sysbuild.cmake)、[samples/tfm_integration/tfm_fwu/sysbuild.conf](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/tfm_integration/tfm_fwu/sysbuild.conf)、[samples/tfm_integration/tfm_fwu/tests.yaml](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/tfm_integration/tfm_fwu/tests.yaml)、[samples/tfm_integration/tfm_fwu/swapped_app/src/main.c](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/tfm_integration/tfm_fwu/swapped_app/src/main.c)。

本仓库的[对应源码](../../../samples/tfm_integration/tfm_fwu/src/main.c)可用于跟踪，版本可能与网页不同；本批仅翻译和核对文档，没有执行固件构建、烧录、密钥生成或存储操作。

<a id="tfm_fwu"></a>
<a id="overview"></a>
<a id="building-and-running"></a>
<a id="sample-output"></a>

[上一章](P009_PSA受保护存储示例.md) · [返回大纲](大纲.md) · [下一章](P011_PSA架构测试示例.md)
