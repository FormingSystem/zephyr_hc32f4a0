---
id: learning.zephyr-docs.tfm.page-7
title: TFM集成示例目录
kind: reference
status: maintained
domains: [zephyr, tfm, security]
source_url: https://docs.zephyrproject.org/latest/samples/tfm_integration/tfm_integration.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第7章\_TFM集成示例目录

原文：[官方页面](https://docs.zephyrproject.org/latest/samples/tfm_integration/tfm_integration.html)。读取日期：2026-10-14；保存的 latest 页面及 HTML 摘要见[来源记录](../SOURCES.md)。

## 7.1\_TF-M 集成示例（TF-M Integration）

这些 TF-M 集成示例适用于受支持的 Armv8-M 开发板，展示如何在 Zephyr 中使用 TF-M API。

| 官方示例 | 功能 |
| --- | --- |
| [TF-M 固件更新（Firmware Update）](P010_TFM固件更新示例.md#tfm_fwu) | 使用 PSA 固件更新 API 执行固件更新。 |
| [TF-M 进程间通信（Inter-Process Communication，IPC）](../intercore_reference/P191_TFM的IPC服务示例.md#tfm_ipc) | 使用 IPC 实现安全镜像与非安全镜像之间的通信。 |
| [TF-M PSA 密码功能（Crypto）](P008_PSA密码示例.md#tfm_psa_crypto) | 使用 PSA Crypto API 执行密码运算，以及生成设备证书签名请求（Certificate Signing Request，CSR）。 |
| [TF-M PSA 受保护存储（Protected Storage，PS）](P009_PSA受保护存储示例.md#psa_protected_storage) | 使用 PS API 存储加密数据。 |
| [TF-M 安全分区（Secure Partition）](P012_TFM安全分区示例.md#tfm_secure_partition) | 创建对外提供安全服务的安全分区。 |

## 7.2\_概述（Overview）

可信固件的平台安全架构（Platform Security Architecture，PSA）API 用于安全处理环境（S），Zephyr 则运行在非安全处理环境（NS）中。

标准构建过程通常除生成 TF-M 安全镜像与 Zephyr 非安全镜像外，还会构建安全引导加载程序 BL2。随后合并 S 与 NS 镜像并用私钥签名，对应公钥保存在安全引导加载程序中。这样，在启动时的镜像验证过程中，就可以依据由开发者控制的密钥对验证应用镜像，并决定接受或拒绝它们。

## 7.3\_什么是可信固件 M（Trusted Firmware-M，TF-M）

TF-M 是[平台安全架构（Platform Security Architecture，PSA）](https://pages.arm.com/psa-resources.html)的参考实现。

TF-M 提供可高度配置的软件组件，通过安全存储（Secure Storage）、密码服务（Cryptography）、审计日志（Audit Logs）及证明服务（Attestation）等安全运行时服务，建立可信执行环境（Trusted Execution Environment，TEE）。此外，TF-M 的安全引导（Secure Boot）确保运行时软件的完整性，并支持固件升级。

原文说明，当前 TF-M 实现专门面向 ARMv8-M 的 TrustZone。

TF-M 源码位于 [git.trustedfirmware.org](https://git.trustedfirmware.org)。为方便集成，Zephyr 项目也将其分支作为模块维护在 [Zephyr 的 TF-M 模块仓库](https://github.com/zephyrproject-rtos/trusted-firmware-m)。

译注：原文的 Trusted Firmware Git 站点本次返回访问限制／浏览器验证页，自动核验未通过；保留原链接供对照，Zephyr 维护的模块链接可正常访问。

更多信息见 [TF-M 官方文档](https://tf-m.docs.trustedfirmware.org/en/latest/)。

译注：本页是示例目录，正文译完不代表各个示例或外部 TF-M 文档已全部翻译。板级支持、默认安全服务与构建行为应以所用 Zephyr／TF-M 修订为准；继续阅读本册的[环境要求](P003_TFM环境与硬件要求.md)、[构建系统](P004_TFM构建系统.md)与[集成说明](P005_TFM与Zephyr集成.md)。


<a id="tf-m-integration"></a>
<a id="overview"></a>
<a id="what-is-trusted-firmware-m-tf-m"></a>

[上一章](P006_TFM测试套件.md) · [返回大纲](大纲.md) · [下一章](P008_PSA密码示例.md)
