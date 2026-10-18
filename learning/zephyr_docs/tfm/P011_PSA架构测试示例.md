---
id: learning.zephyr-docs.tfm.page-11
title: PSA架构测试示例
kind: reference
status: maintained
domains: [zephyr, tfm, security]
source_url: https://docs.zephyrproject.org/latest/samples/tfm_integration/tfm_psa_test/README.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第11章\_PSA架构测试示例

原文：[官方页面](https://docs.zephyrproject.org/latest/samples/tfm_integration/tfm_psa_test/README.html)。读取日期：2026-10-14；保存的 latest 页面及 HTML 摘要见[来源记录](../SOURCES.md)。

## 11.1\_概述（Overview）

本示例使用 Zephyr 与 TF-M 运行平台安全架构（Platform Security Architecture，PSA）测试套件。测试实现在 [psa-arch-tests 官方仓库](https://github.com/ARM-software/psa-arch-tests)中。

示例支持已经在 `psa-arch-tests` 中完成移植的平台，具体平台列表见示例的 `tests.yaml`。

## 11.2\_构建与运行（Building and Running）

必须通过 `CONFIG_TFM_PSA_TEST_*` 配置选择测试套件。每次只能运行一组，由下列 Kconfig 选项之一指定：

| 配置选项 | 测试内容 |
| --- | --- |
| `CONFIG_TFM_PSA_TEST_CRYPTO` | 密码服务（Crypto） |
| `CONFIG_TFM_PSA_TEST_PROTECTED_STORAGE` | 受保护存储（Protected Storage，PS） |
| `CONFIG_TFM_PSA_TEST_INTERNAL_TRUSTED_STORAGE` | 内部可信存储（Internal Trusted Storage，ITS） |
| `CONFIG_TFM_PSA_TEST_STORAGE` | 存储测试（Storage），包含相应的 PS／ITS 测试 |
| `CONFIG_TFM_PSA_TEST_INITIAL_ATTESTATION` | 初始证明（Initial Attestation） |

可在构建时通过配置参数指定需要的套件：

```sh
$ west build samples/tfm_integration/tfm_psa_test/ \
  -p -b mps2/an521/cpu0/ns -t run -- \
  -DCONFIG_TFM_PSA_TEST_STORAGE=y
```

并不是所有开发板都支持全部测试套件。

译注：命令在已准备好 TF-M、`psa-arch-tests` 模块及目标工具链的 Zephyr 源码根目录执行，`$` 为原文终端提示符。当前官方 `tests.yaml` 的自动测试列表对部分平台排除密码测试，并注释停用初始证明测试项；其注释说明原因涉及 `t_cose` 使用的 QCBOR 库许可问题。原页选项列表与当前自动测试启用状态是不同信息，需按所用修订核对。

### 11.2.1\_在目标板上运行（On Target）

详细步骤参见 [TF-M IPC 示例](../intercore_reference/P191_TFM的IPC服务示例.md#tfm_ipc)。

### 11.2.2\_在 QEMU 上运行（On QEMU）

详细步骤同样参见 [TF-M IPC 示例](../intercore_reference/P191_TFM的IPC服务示例.md#tfm_ipc)。使用 `west build` 的示例如下：

```sh
$ west build samples/tfm_integration/tfm_psa_test/ -p -b mps2/an521/cpu0/ns -t run -- -DCONFIG_TFM_PSA_TEST_STORAGE=y
```

## 11.3\_示例输出（Sample Output）

```text
*** Booting Zephyr OS build zephyr-v2.5.0-456-g06f4da459a99  ***

***** PSA Architecture Test Suite - Version 1.0 *****

Running.. Storage Suite
******************************************

TEST: 401 | DESCRIPTION: UID not found check
[Info] Executing tests from non-secure

[Info] Executing ITS tests
[Check 1] Call get API for UID 6 which is not set
[Check 2] Call get_info API for UID 6 which is not set
[Check 3] Call remove API for UID 6 which is not set
[Check 4] Call get API for UID 6 which is removed
[Check 5] Call get_info API for UID 6 which is removed
[Check 6] Call remove API for UID 6 which is removed
Set storage for UID 6
[Check 7] Call get API for different UID 5
[Check 8] Call get_info API for different UID 5
[Check 9] Call remove API for different UID 5

[Info] Executing PS tests
[Check 1] Call get API for UID 6 which is not set
[Check 2] Call get_info API for UID 6 which is not set
[Check 3] Call remove API for UID 6 which is not set
[Check 4] Call get API for UID 6 which is removed
[Check 5] Call get_info API for UID 6 which is removed
[Check 6] Call remove API for UID 6 which is removed
Set storage for UID 6
[Check 7] Call get API for different UID 5
[Check 8] Call get_info API for different UID 5
[Check 9] Call remove API for different UID 5

TEST RESULT: PASSED

******************************************

[...]

TEST: 417 | DESCRIPTION: Storage assest capacity modification check
[Info] Executing tests from non-secure

[Info] Executing PS tests
Test Case skipped as Optional PS APIs not are supported.

TEST RESULT: SKIPPED (Skip Code=0x0000002B)

******************************************

************ Storage Suite Report **********
TOTAL TESTS     : 17
TOTAL PASSED    : 11
TOTAL SIM ERROR : 0
TOTAL FAILED    : 0
TOTAL SKIPPED   : 6
******************************************

Entering standby..
```

原输出展示存储套件：测试 401 检查不存在、已删除或不同 UID 上的获取、查询信息和删除操作；测试 417 因不支持可选 PS API 而跳过。汇总为 17 项测试、11 项通过、0 项模拟错误、0 项失败和 6 项跳过，随后进入待机。

译注：`TOTAL FAILED : 0` 不表示所有项目都实际执行并通过，还应查看 `TOTAL SKIPPED` 及跳过原因。这里保留原页 Zephyr 版本与测试输出，未实际运行测试，也不代表已取得 PSA 认证。


译注核对来源：[samples/tfm_integration/tfm_psa_test/src/main.c](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/tfm_integration/tfm_psa_test/src/main.c)、[samples/tfm_integration/tfm_psa_test/prj.conf](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/tfm_integration/tfm_psa_test/prj.conf)、[samples/tfm_integration/tfm_psa_test/tests.yaml](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/tfm_integration/tfm_psa_test/tests.yaml)。

本仓库的[对应源码](../../../samples/tfm_integration/tfm_psa_test/src/main.c)可用于跟踪，版本可能与网页不同；本批仅翻译和核对文档，没有执行固件构建、烧录、密钥生成或存储操作。

<a id="tf-m-platform-security-architecture-test-sample"></a>
<a id="tfm-psa-test"></a>
<a id="overview"></a>
<a id="building-and-running"></a>
<a id="on-target"></a>
<a id="on-qemu"></a>
<a id="sample-output"></a>

[上一章](P010_TFM固件更新示例.md) · [返回大纲](大纲.md) · [下一章](P012_TFM安全分区示例.md)
