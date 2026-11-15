---
id: learning.zephyr-docs.tfm.page-2
title: TFM体系概述
kind: reference
status: maintained
domains: [zephyr, tfm, security]
source_url: https://docs.zephyrproject.org/latest/services/tfm/overview.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第2章\_TFM体系概述

原文：[官方页面](https://docs.zephyrproject.org/latest/services/tfm/overview.html)。读取日期：2026-10-14；保存的 latest 页面及 HTML 摘要见[来源记录](../SOURCES.md)。

## 2.1\_概述

[可信固件 M（Trusted Firmware-M，TF-M）](https://tf-m.docs.trustedfirmware.org/en/latest/) 是平台安全架构（Platform Security Architecture，PSA）[物联网安全框架（IoT Security Framework）](https://www.psacertified.org/what-is-psa-certified/)的参考实现（Reference Implementation）。它定义并实现了一套体系结构和软件组件，以应对物联网产品中的主要安全问题。

原文说明：Zephyr RTOS 自 Zephyr 2.0.0 与 TF-M 1.0 组合起获得 PSA 认证，当前集成版本为 TF-M 2.1.0。

译注：这里保留原页的版本与认证叙述。实际工程使用哪个 TF-M 修订，应以所用 Zephyr 版本的 `west.yml` 和模块内容为准；不能把原文的“当前”自动当作本地工作区版本，也不能把历史认证陈述视为所有开发板／固件配置均已认证。

译注：原页引用的 Arm PSA 资源旧入口在本次核验中遇到证书链问题，暂未确认可访问；链接按原文保留。

## 2.2\_TF-M 提供什么

TF-M 通过其架构设计和一组安全服务（Secure Services）提供：

- 安全与非安全资源隔离。
- 适合嵌入式系统的密码功能。
- 设备秘密数据（密钥等）的管理。
- 固件验证及加密。
- 受保护的片外数据存储与读取。
- 设备身份证明，即设备证明（Device Attestation）。
- 审计日志（Audit Logging）。

## 2.3\_构建系统集成

在受支持的平台上使用 TF-M 时，标准 Zephyr 构建过程会在后台自动构建并链接 TF-M。此流程对 TF-M 的使用方式作出了一些假定，也会影响 Zephyr 应用映像能做什么：

- 安全处理环境（Secure Processing Environment，SPE），包括安全启动和 TF-M，首先启动。
- Zephyr 的资源分配依赖安全映像作出的选择。

## 2.4\_体系结构概述（Architecture Overview）

通常，TF-M 应用包含以下三个部分。下图从左到右按信任程度由高到低排列，执行顺序也相同：安全启动 → 安全映像 → 非安全映像。

安全引导加载程序（Secure Bootloader）是可选的，但默认启用；安全启动是构成安全方案的重要部分。

```text
+-------------------------------------+           +--------------+
| Secure Processing Environment (SPE) |           |     NSPE     |
| +----------++---------------------+ |           | +----------+ |
| |          ||                     | |           | |          | |
| | bl2.bin  ||  tfm_s_signed.bin   | |           | |zephyr.bin| |
| |          ||                     | | <- PSA -> | |          | |
| |  Secure  || Trusted Firmware-M  | |    APIs   | |  Zephyr  | |
| |   Boot   ||   (Secure Image)    | |           | |(NS Image)| |
| |          ||                     | |           | |          | |
| +----------++---------------------+ |           | +----------+ |
+-------------------------------------+           +--------------+
```

图中文字：SPE 为安全处理环境；NSPE 为非安全处理环境（Non-Secure Processing Environment）；Secure Boot 为安全启动；Secure Image 为安全映像；NS Image 为非安全映像。`bl2.bin`、`tfm_s_signed.bin` 与 `zephyr.bin` 分别对应图中的三个执行部分。

Zephyr 的非安全处理环境与 TF-M 的安全处理环境映像，通过一组 PSA API 通信。通常使用随 TF-M 一起构建、并在 Zephyr 中实现的进程间通信机制（Inter-Process Communication，IPC），参阅 [modules/trusted-firmware-m/interface](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/trusted-firmware-m/interface)。

### 2.4.1\_信任根架构（Root of Trust Architecture）

TF-M 基于信任根（Root of Trust，RoT）架构，建立从最高信任到较低、最低信任的层级，为构建和访问可信服务与资源提供基础。

这种方式防止低信任组件访问或破坏系统中更关键的部分，也使低信任环境中的错误不会损坏已隔离的高信任资源。

TF-M 定义的信任层级由高到低为：

1. PSA 信任根（PSA Root of Trust，PRoT），包括不可变 PSA 信任根（PSA Immutable Root of Trust，即安全启动）和可更新 PSA 信任根（PSA Updateable Root of Trust，即最高信任的安全服务）。
2. 应用信任根（Application Root of Trust，ARoT），即隔离的安全服务。

不可变 PSA 信任根是系统中最受信任的代码，后续信任根都以它为基础。在 TF-M 中，它对应安全启动映像，验证安全与非安全映像有效、未遭篡改且来自可靠来源。安全引导程序利用内置的公钥，在固件更新时验证新映像。正如名称所示，此映像不可变。

可更新 PSA 信任根实现 TF-M 中最受信任的安全服务与组件，例如安全分区管理器（Secure Partition Manager，SPM）、PSA Crypto 和内部可信存储（Internal Trusted Storage，ITS）等共享服务。此信任根中的服务可以访问同一信任根内的其他资源。

应用信任根是安全处理环境内权限较低的区域。其对 PRoT 的访问受到所选隔离级别限制；最高隔离级别还限制不同 ARoT 服务之间的访问。受保护存储（Protected Storage，PS）等标准服务位于 ARoT。自定义安全服务通常也应放在 ARoT，除非有充分理由放进 PRoT。

这些区域与在非安全环境中运行的不可信代码相区分。非安全代码在系统中权限最低，在这里就是 Zephyr 应用映像。

### 2.4.2\_隔离级别（Isolation Levels）

TF-M 定义三种边界逐渐严格的隔离级别，具体选择取决于安全需求与可用系统资源。

- **隔离级别 1**：最低级别，主要边界仅存在于安全和非安全处理环境之间，通常通过 Armv8-M 的 Arm TrustZone 实现。可更新 PRoT 与 ARoT 不作区分，在相同特权级执行；组合映像大小最小。
- **隔离级别 2**：在级别 1 基础上区分可更新 PRoT 与 ARoT。ARoT 对 PRoT 的访问受限，只能通过 PRoT 服务公开的 API 通信；但 ARoT 服务相互之间尚未严格隔离。
- **隔离级别 3**：最高级别。在级别 2 基础上再隔离各 ARoT 服务，使每个 ARoT 服务与其他服务相互分离。这提供最高隔离程度，也带来额外开销和服务间代码重复。

通过 [`CONFIG_TFM_ISOLATION_LEVEL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_TFM_ISOLATION_LEVEL) 查看当前隔离级别。

## 2.5\_安全启动（Secure Boot）

TF-M 默认的安全引导程序基于 [MCUBoot](https://www.mcuboot.com/)，在 TF-M 中称为 BL2，即第二阶段引导加载程序（Second-stage Bootloader）；在它之前，安全 MCU 可能还有硬件引导程序。

TF-M 中的映像经过散列和签名，在固件更新时由 MCUboot 验证散列值与签名。

TF-M 所用 MCUboot 的主要特性如下：

- 公共签名密钥内置于引导程序。
- 安全（S）与非安全（NS）映像可以使用不同密钥签名。
- 固件映像可选加密。
- 客户端软件负责把新映像写入次级槽（Secondary Slot）。
- 默认采用包含两个等大存储区域的静态闪存布局。
- 可选安全计数器（Security Counter）用于回滚保护（Rollback Protection）。

对可选的映像加密，原文说明：只有载荷（Payload）加密，头部和标签—长度—值（Tag-Length-Value，TLV）保持明文；散列与签名作用于未加密数据；加密采用 AES-CTR-128 或 AES-CTR-256；`imgtool` 在每次加密时随机生成加密密钥。

AES-CTR 密钥包含在映像内，并可使用以下方式加密：RSA-OAEP、AES 密钥封装（AES Key Wrap，AES-KW，根据 AES-CTR 密钥长度选择 128 或 256 位）、椭圆曲线集成加密方案（Elliptic Curve Integrated Encryption Scheme，ECIES）的 `ECIES-P256` 或 `ECIES-X25519` 形式。

Zephyr 中控制安全启动的关键配置为：

- [`CONFIG_TFM_BL2`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_TFM_BL2)：启用／关闭引导程序，原文默认值为 `y`。
- [`CONFIG_TFM_KEY_FILE_S`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_TFM_KEY_FILE_S)：覆盖安全映像签名密钥。
- [`CONFIG_TFM_KEY_FILE_NS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_TFM_KEY_FILE_NS)：覆盖非安全映像签名密钥。

## 2.6\_安全处理环境（Secure Processing Environment）

安全引导程序执行完毕后，基于 TF-M 的安全映像开始在 SPE 中执行，完成设备初始配置及安全服务初始化。

设备起始状态由安全固件控制。因此，非安全 Zephyr 应用启动时，外设未必处于硬件默认复位状态。如有疑问，应查看 TF-M 模块 `platform/ext/target/` 中的板级支持包（Board Support Package，BSP）；在默认 Zephyr west 工作区中，TF-M 模块位于 `modules/tee/tf-m/trusted-firmware-m/`。

### 2.6.1\_安全服务（Secure Services）

截至原文引用的 TF-M 1.8.0，通常提供以下服务，但厂商支持情况可能不同：密码服务（Crypto）、固件更新（Firmware Update，FWU）、初始证明（Initial Attestation）、平台服务（Platform），以及包含 ITS 和 PS 两部分的安全存储（Secure Storage）。

另有用于创建自定义服务的模板。服务详情与公开 API 见 [TF-M 官方文档](https://tf-m.docs.trustedfirmware.org/en/latest/)。

### 2.6.2\_密钥管理与派生（Key Management and Derivation）

密钥与秘密数据管理是安全设备的重要部分。必须使密钥材料仅对需要它的区域可用，并以难以篡改或恶意访问的方式安全保存。

TF-M 的 PSA Crypto 服务使用 ITS 存储密钥，并利用 Mbed TLS 执行密码功能，确保私钥仅可被安全处理环境访问。签名载荷、解密敏感数据等使用密钥的操作通过密钥句柄（Key Handle）执行；密钥材料不应暴露给非安全环境。

一个例外是可以通过单向操作向安全环境预配私钥，例如在工厂预配阶段。不过，应尽可能避免这种做法；更好的方式是请求 SPE 通过 PSA Crypto 自行生成私钥，在预配时只取出公钥并在工厂记录。这样私钥材料从未暴露，预配方也不知道它。

TF-M 还大量使用每台 TF-M 设备必须提供的硬件唯一密钥（Hardware Unique Key，HUK）。例如，PS 用此设备专属密钥保护外部存储的信息。每台设备使用自己的 HUK，因此将闪存取下并放到另一设备上，也无法用另一设备的密钥解密原内容。

HUK 还可用于派生新密钥。派生密钥无需保存，因为启动时可结合额外的盐值／种子（Salt/Seed，取决于密钥派生算法）从 HUK 重新生成，从而减少存储问题与常见攻击入口。安全设备中的 HUK 通常受到严格保护，用户无法直接访问。

软件实现使用 `TFM_CRYPTO_ALG_HUK_DERIVATION` 标识默认密钥派生算法。原文的默认算法为基于 SHA-256 的 HKDF（HMAC-based Extract-and-Expand Key Derivation Function，基于 HMAC 的提取与扩展密钥派生函数），定义见 [RFC 5869](https://datatracker.ietf.org/doc/html/rfc5869.html)。部分平台可能提供其他硬件实现。

## 2.7\_非安全处理环境（Non-Secure Processing Environment）

在 TF-M 支持的开发板上启用 [`CONFIG_BUILD_WITH_TFM`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BUILD_WITH_TFM)，即可让 Zephyr 用于 NSPE。

通常只需选择有效开发板的 `*/ns` 目标，例如 `mps2/an521/cpu0/ns`。构建过程会把 Zephyr 配置为在 NSPE 运行，正确构建并链接 TF-M 安全映像，对安全与非安全映像签名，并将三个二进制合成 `tfm_merged.hex`。此配置下，[west flash](../west/P007_构建烧录与调试.md#west-flashing) 默认烧录 `tfm_merged.hex`。

原文说明，目前此集成方式不能把 Zephyr 配置为 TF-M 的安全处理环境。

译注：这里说明的是 Zephyr 与 TF-M 的职责划分，不能扩大为“Zephyr 永远不能在处理器安全状态执行”。本册讨论的受支持组合由 TF-M 提供 SPE、Zephyr 提供 NSPE。原图与上述路径均属于官方布局；工作区前缀由读者实际位置决定。


译注核对来源：[west.yml](https://github.com/zephyrproject-rtos/zephyr/blob/main/west.yml)。

本仓库的[对应源码](../../../west.yml)可用于跟踪，版本可能与网页不同；本批仅翻译和核对文档，没有执行固件构建、烧录、密钥生成或存储操作。

<a id="trusted-firmware-m-overview"></a>
<a id="what-does-tf-m-offer"></a>
<a id="build-system-integration"></a>
<a id="architecture-overview"></a>
<a id="root-of-trust-rot-architecture"></a>
<a id="isolation-levels"></a>
<a id="secure-boot"></a>
<a id="secure-processing-environment"></a>
<a id="secure-services"></a>
<a id="key-management-and-derivation"></a>
<a id="index-0"></a>
<a id="non-secure-processing-environment"></a>

<!-- reading-navigation:start -->

**主线阅读**

[上一篇：TFM可信固件入口](P001_TFM可信固件入口.md) · [本模块主线目录](../reading/tfm.md) · [全部主线](../reading/README.md) · [下一篇：TFM环境与硬件要求](P003_TFM环境与硬件要求.md)

<details>
<summary>原册编号导航（含扩展参考）</summary>

[上一章](P001_TFM可信固件入口.md) · [返回大纲](大纲.md) · [下一章](P003_TFM环境与硬件要求.md)

</details>

<!-- reading-navigation:end -->
