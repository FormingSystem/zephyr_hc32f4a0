---
id: learning.zephyr-docs.tfm.page-9
title: PSA受保护存储示例
kind: reference
status: maintained
domains: [zephyr, tfm, security]
source_url: https://docs.zephyrproject.org/latest/samples/tfm_integration/psa_protected_storage/README.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第9章\_PSA受保护存储示例

原文：[官方页面](https://docs.zephyrproject.org/latest/samples/tfm_integration/psa_protected_storage/README.html)。读取日期：2026-10-14；保存的 latest 页面及 HTML 摘要见[来源记录](../SOURCES.md)。

## 9.1\_概述（Overview）

本示例展示如何用受保护存储（Protected Storage，PS）API 保存数据。

PS 提供键值存储接口（Key/Value Storage Interface），默认对数据加密，并可选提供认证（Authentication）和回滚保护（Rollback Protection）。原文默认密码算法为 AES-128-GCM，即采用 128 位密钥的高级加密标准伽罗瓦／计数器模式（Advanced Encryption Standard, Galois/Counter Mode）。加密密钥派生自硬件唯一密钥（Hardware Unique Key，HUK），HUK 通常通过设备熔丝等方式设置。

本示例通过 PS API 将数据写入非易失存储（Non-Volatile Storage），展示如何使用唯一标识符（Unique Identifier，UID）保存和读取数据，以及如何通过标志启用覆盖写保护（Overwrite Protection）。

TF-M 通过 `PS_NUM_ASSETS` 限制 PS 记录数量，通过 `PS_MAX_ASSET_SIZE` 限制单条记录大小。原文以 TF-M 1.3.0 为例，默认分别为 10 和 2048。不同平台的默认值可能不同；TF-M 编译阶段会打印当前值。

关于 PS 的更多信息，参见平台安全架构（Platform Security Architecture，PSA）的安全存储 API：[Arm 平台安全入口](https://developer.arm.com/architectures/architecture-security-features/platform-security)。

本示例适用于 [trusted-firmware-m 仓库](https://git.trustedfirmware.org/TF-M/trusted-firmware-m.git/)支持的平台；具体平台列表见示例的 `tests.yaml`。

译注：上述 Arm 平台安全旧入口在本次自动核验中出现证书链问题，暂未确认可访问，保留原链接作为来源。

## 9.2\_构建与运行（Building and Running）

### 9.2.1\_在目标板上运行（On Target）

原文要求在烧录示例之前完整擦除开发板，因为所用 Flash 区域可能有残留数据；每次重新运行示例之前也要擦除，因为断电复位不会解除覆盖写保护。

译注：这是原示例对持久存储初始状态的要求，擦除会丢失既有数据。当前源码先写入并读取 UID1，再覆盖它；随后用 `PSA_STORAGE_FLAG_WRITE_ONCE` 创建 UID2，预期再次写 UID2 返回 `PSA_ERROR_NOT_PERMITTED`。结尾只删除 UID1，UID2 保留，因此单纯复位无法回到初次运行的存储状态。本次仅翻译和核对，没有执行擦除或写入。

### 9.2.2\_在 QEMU 上运行（On QEMU）

详细步骤参见 [TF-M IPC 示例](../intercore_reference/P191_TFM的IPC服务示例.md#tfm_ipc)。以下是使用 `west build` 的示例，从 Zephyr 源码根目录执行，前提是主机工具、TF-M 依赖与目标工具链已就绪。

```sh
$ west build samples/tfm_integration/psa_protected_storage/ -p -b mps2/an521/cpu0/ns -t run
```

## 9.3\_示例输出（Sample Output）

```text
*** Booting Zephyr OS build zephyr-v2.5.0-2791-g5585355dde0c  ***
TF-M Protected Storage sample started. PSA Protected Storage API Version 1.0
Writing data to UID1: The quick brown fox jumps over the lazy dog
Info on data stored in UID1:
- Size: 16
- Capacity: 0x42
- Flags: 0x 0
Read and compare data stored in UID1
Data stored in UID1: The quick brown fox jumps over the lazy dog
Overwriting data stored in UID1 with: Lorem ipsum dolor sit amet
Writing data to UID2 with overwrite protection: The quick brown fox jumps over the lazy dog
Attempting to write 'The quick brown fox jumps over the lazy dog' to UID2
Got expected error (PSA_ERROR_NOT_PERMITTED) when writing to protected UID
Removing UID1
```

日志展示 UID1 的写入、属性读取、数据读取与覆盖，随后创建带写保护的 UID2，验证写入被拒绝，最后删除 UID1。

译注：这是原页旧版输出，包含 `Size: 16`、`Capacity: 0x42` 等原始数值，不能据此推断当前源码中测试字符串的实际长度。当前源码使用 `sizeof(TEST_STRING_1)` 写入字符串，含结尾空字符；第二次尝试写 UID2 时使用的是 `TEST_STRING_2`。日志和源码之间的这些差异按各自来源保留。


译注核对来源：[samples/tfm_integration/psa_protected_storage/src/main.c](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/tfm_integration/psa_protected_storage/src/main.c)、[samples/tfm_integration/psa_protected_storage/prj.conf](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/tfm_integration/psa_protected_storage/prj.conf)、[samples/tfm_integration/psa_protected_storage/tests.yaml](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/tfm_integration/psa_protected_storage/tests.yaml)。

本仓库的[对应源码](../../../samples/tfm_integration/psa_protected_storage/src/main.c)可用于跟踪，版本可能与网页不同；本批仅翻译和核对文档，没有执行固件构建、烧录、密钥生成或存储操作。

<a id="psa_protected_storage"></a>
<a id="overview"></a>
<a id="building-and-running"></a>
<a id="on-target"></a>
<a id="on-qemu"></a>
<a id="sample-output"></a>

[上一章](P008_PSA密码示例.md) · [返回大纲](大纲.md) · [下一章](P010_TFM固件更新示例.md)
