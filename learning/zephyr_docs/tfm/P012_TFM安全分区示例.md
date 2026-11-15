---
id: learning.zephyr-docs.tfm.page-12
title: TFM安全分区示例
kind: reference
status: maintained
domains: [zephyr, tfm, security]
source_url: https://docs.zephyrproject.org/latest/samples/tfm_integration/tfm_secure_partition/README.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第12章\_TFM安全分区示例

原文：[官方页面](https://docs.zephyrproject.org/latest/samples/tfm_integration/tfm_secure_partition/README.html)。读取日期：2026-10-14；保存的 latest 页面及 HTML 摘要见[来源记录](../SOURCES.md)。

## 12.1\_概述（Overview）

安全分区（Secure Partition）是位于 TF-M 内部的隔离模块，向其他分区和／或非安全固件提供一组函数，也就是安全服务（Secure Services）。TF-M 已包含 `crypto`、`protected_storage`、`firmware_update` 等标准分区，也允许创建自定义分区。

本示例创建一个演示安全分区及安全服务，并指示 TF-M 构建系统将其编入安全固件；非安全固件的主程序随后调用该服务。

这个演示分区只有一个安全服务：根据索引选择分区内 5 个演示秘密值之一，并取得该秘密值的散列摘要（Hash Digest）。

分区位于示例的 `dummy_partition` 目录，其中包含分区源码、构建文件和构建配置，由 TF-M 构建系统负责构建。详情见 [TF-M 构建系统](P004_TFM构建系统.md#tfm-build-system)。

关于添加自定义安全分区，参见 [TF-M 安全分区添加指南](https://tf-m.docs.trustedfirmware.org/en/latest/integration_guide/services/tfm_secure_partition_addition.html)。

将本分区改作自用时，应把所有 `dummy_partition`、`DUMMY_PARTITION`、`dp` 与 `DP` 替换为自己的分区名称；同时检查安全侧和非安全侧的 `CMakeLists.txt`，以及原文所称 “partition” 内的 YAML 文件，作相应调整。

译注——源码跟踪：此示例的实际目录名为 `dummy_partition`。应用侧 CMake 从两个 `.yaml.in` 模板生成清单，通过 `TFM_CMAKE_OPTIONS` 将 `TFM_EXTRA_MANIFEST_LIST_FILES` 和 `TFM_EXTRA_PARTITION_PATHS` 传给 TF-M；这决定安全分区如何加入安全镜像。只修改非安全侧函数名不足以完成自定义服务接入。

## 12.2\_构建与运行（Building and Running）

本示例包含两种模式对应的代码，可以选择 [`CONFIG_TFM_IPC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_TFM_IPC) 或 [`CONFIG_TFM_SFN`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_TFM_SFN) 构建。前者采用进程间通信（Inter-Process Communication，IPC），后者采用安全函数（Secure Function，SFN）方式。

### 12.2.1\_在目标板上运行（On Target）

详细步骤参见 [TF-M IPC 示例](../intercore_reference/P191_TFM的IPC服务示例.md#tfm_ipc)。

### 12.2.2\_在 QEMU 上运行（On QEMU）

详细步骤参见 [TF-M IPC 示例](../intercore_reference/P191_TFM的IPC服务示例.md#tfm_ipc)，实际应用目录应选择本示例 `samples/tfm_integration/tfm_secure_partition`；工具链、TF-M 模块与受支持非安全板级目标需先准备好。

## 12.3\_示例输出（Sample Output）

```text
*** Booting Zephyr OS build zephyr-v3.0.0-3061-g9bb87f4d46e9  ***
Digest: be45cb2605bf36bebde684841a28f0fd43c69850a3dce5fedba69928ee3a8991
Digest: 1452c8f04245d355722fdbfb03c69bcfd380b7dff911a3e425013397251f6a4e
Digest: d3b4349010abb691b9584b6fd6b41ec54596ef7b98d853fb4f5bfa690f50f222
Digest: 5afbcfede855ca834ff5b4e8a44a32206a51381f3cf52f5001a3241f017ac41a
Digest: 983318380c325099da63de2e7ca57c1630693b28b4754e08817533295dbfcfbb
No valid secret for key, received expected error code
```

输出中的 `Digest` 表示摘要；最后一句表示该索引没有有效秘密值，收到预期错误码。

译注：当前源码中的 5 个秘密值均为公开演示数据，每个 16 字节；安全服务计算 SHA-256，要求输出长度为 32 字节。主程序依次请求索引 0～5，前 5 项打印摘要，第 6 项超出有效索引范围，预期返回 `PSA_ERROR_INVALID_ARGUMENT`。因此示例演示的是跨安全边界的服务调用与参数检查，不能把公开的演示数据当作真实设备秘密。原日志保留，未运行固件。


译注核对来源：[samples/tfm_integration/tfm_secure_partition/src/main.c](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/tfm_integration/tfm_secure_partition/src/main.c)、[samples/tfm_integration/tfm_secure_partition/src/dummy_partition.c](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/tfm_integration/tfm_secure_partition/src/dummy_partition.c)、[samples/tfm_integration/tfm_secure_partition/dummy_partition/dummy_partition.c](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/tfm_integration/tfm_secure_partition/dummy_partition/dummy_partition.c)、[samples/tfm_integration/tfm_secure_partition/CMakeLists.txt](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/tfm_integration/tfm_secure_partition/CMakeLists.txt)、[samples/tfm_integration/tfm_secure_partition/dummy_partition/CMakeLists.txt](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/tfm_integration/tfm_secure_partition/dummy_partition/CMakeLists.txt)、[samples/tfm_integration/tfm_secure_partition/dummy_partition/tfm_dummy_partition.yaml.in](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/tfm_integration/tfm_secure_partition/dummy_partition/tfm_dummy_partition.yaml.in)、[samples/tfm_integration/tfm_secure_partition/tests.yaml](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/tfm_integration/tfm_secure_partition/tests.yaml)。

本仓库的[对应源码](../../../samples/tfm_integration/tfm_secure_partition/src/main.c)可用于跟踪，版本可能与网页不同；本批仅翻译和核对文档，没有执行固件构建、烧录、密钥生成或存储操作。

<a id="tfm_secure_partition"></a>
<a id="overview"></a>
<a id="building-and-running"></a>
<a id="on-target"></a>
<a id="on-qemu"></a>
<a id="sample-output"></a>

[上一章](P011_PSA架构测试示例.md) · [返回大纲](大纲.md)
