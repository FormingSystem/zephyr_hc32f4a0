---
id: learning.zephyr-docs.tfm.page-6
title: TFM测试套件
kind: reference
status: maintained
domains: [zephyr, tfm, security]
source_url: https://docs.zephyrproject.org/latest/services/tfm/testsuites.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第6章\_TFM测试套件

原文：[官方页面](https://docs.zephyrproject.org/latest/services/tfm/testsuites.html)。读取日期：2026-10-14；保存的 latest 页面及 HTML 摘要见[来源记录](../SOURCES.md)。

## 6.1\_测试套件概览（Test Suites）

TF-M 包含两组测试套件：

- `tf-m-tests`：TF-M 专用的标准回归测试（Regression Tests）。
- `psa-arch-tests`：面向特定平台安全架构（Platform Security Architecture，PSA）API 的测试，例如安全存储接口。

可通过 `samples/tfm_integration` 目录中的适当示例应用，从 Zephyr 运行这些测试套件。

## 6.2\_TF-M 回归测试（TF-M Regression Tests）

回归测试套件可通过 [tests/modules/tf-m/regression](https://github.com/zephyrproject-rtos/zephyr/blob/main/tests/modules/tf-m/regression) 测试运行。

它通过 PSA API 检查跨越非安全／安全（Non-Secure/Secure，NS/S）边界的各类服务与通信机制，为非安全 RTOS（此处为 Zephyr）和安全应用（TF-M）的正确集成提供基本健全性检查（Sanity Check）。

## 6.3\_PSA 架构测试（PSA Arch Tests）

[TF-M 平台安全架构测试示例](P011_PSA架构测试示例.md#tfm-psa-test)提供 PSA Arch Test 套件。其中包含多组测试，用于验证安全应用是否遵循 PSA API 规范；TF-M 是 PSA 的一种实现。

每次只能运行其中一组测试，可用测试套件由 `CONFIG_TFM_PSA_TEST_*` Kconfig 选项描述。

### 6.3.1\_用途（Purpose）

为特定开发板、RTOS（这里为 Zephyr）以及 PSA 实现（这里为 TF-M）的组合获取 PSA 认证，需要这些测试套件的输出。

它们也有助于验证对 TF-M 作出实质修改的拉取请求（Pull Request，PR），例如启用新 TF-M 板级目标，或修改核心 TF-M 模块。发布新增板级支持等 PR 之前，通常应先运行它们，检查各部分能否一致工作。

译注：测试输出是原文所述认证过程需要的材料，单独运行通过不等于该产品已取得认证。具体测试选择与适用平台应核对所用版本的测试配置和定义；本次只核对文档与源码，没有运行测试或声称板级验证通过。


译注核对来源：[tests/modules/tf-m/regression/prj.conf](https://github.com/zephyrproject-rtos/zephyr/blob/main/tests/modules/tf-m/regression/prj.conf)、[tests/modules/tf-m/regression/tests.yaml](https://github.com/zephyrproject-rtos/zephyr/blob/main/tests/modules/tf-m/regression/tests.yaml)。

本仓库的[对应源码](../../../tests/modules/tf-m/regression/prj.conf)可用于跟踪，版本可能与网页不同；本批仅翻译和核对文档，没有执行固件构建、烧录、密钥生成或存储操作。

<a id="test-suites"></a>
<a id="tf-m-regression-tests"></a>
<a id="psa-arch-tests"></a>
<a id="purpose"></a>

<!-- reading-navigation:start -->

**主线阅读**

[上一篇：TFM与Zephyr集成](P005_TFM与Zephyr集成.md) · [本模块主线目录](../reading/tfm.md) · [全部主线](../reading/README.md)

<details>
<summary>原册编号导航（含扩展参考）</summary>

[上一章](P005_TFM与Zephyr集成.md) · [返回大纲](大纲.md) · [下一章](P007_TFM集成示例目录.md)

</details>

<!-- reading-navigation:end -->
