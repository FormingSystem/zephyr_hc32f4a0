---
id: learning.zephyr-docs.crypto.page-3
title: PSA密码学
kind: reference
status: maintained
domains: [zephyr, crypto, security]
source_url: https://docs.zephyrproject.org/latest/services/crypto/psa_crypto.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第3章\_PSA密码学

原文：[官方页面](https://docs.zephyrproject.org/latest/services/crypto/psa_crypto.html)。读取日期：2026-10-14；保存的 latest 页面及 HTML 摘要见[来源记录](../SOURCES.md)。

## 3.1\_概述（Overview）

平台安全架构（Platform Security Architecture，PSA）的密码学 API（PSA Crypto API）为各种硬件上的密码操作和密钥存储提供可移植的编程接口。它旨在易于使用，同时允许访问现代密码学所必需的底层原语（Low-level Primitives）。

该接口由 Arm 创建和维护。Arm 将 PSA 设计为一套综合安全框架，以满足联网设备不断增长的安全需求。

在 Zephyr 中，PSA Crypto API 使用 Mbed TLS 实现。Mbed TLS 是一个开源密码学库，负责提供底层密码功能。

## 3.2\_设计目标（Design Goals）

此接口适用于非常广泛的设备：使用内置密钥处理数据的专用密码处理器、运行定制应用代码的资源受限设备（例如微控制器），以及服务器等多应用设备。它遵循密码敏捷性（Cryptographic Agility）原则。

**算法灵活性（Algorithm Flexibility）**：PSA Crypto API 支持多种密码算法，开发者可按需要在不同密码方法之间切换。随着新算法出现、现有算法过时，这种灵活性对于维持安全性至关重要。

**密钥管理（Key Management）**：API 提供完善的密钥管理功能，以安全、灵活的方式支持密码密钥的创建、存储和使用。它使用不透明密钥标识符（Opaque Key Identifiers），便于在不暴露密钥材料（Key Material）的情况下替换和更新密钥。

**实现独立性（Implementation Independence）**：API 对底层密码库进行抽象，因此具体实现可以变化而不影响应用代码。这种抽象允许按需使用不同的密码库或硬件加速器（Hardware Accelerator），从而支持密码敏捷性。

**面向未来（Future-Proofing）**：遵循密码敏捷性原则，使应用能够快速适应新的密码标准和实践，从而增强长期安全性与合规性。

## 3.3\_应用示例（Examples of Applications）

**网络安全／TLS（Network Security）**：API 提供建立传输层安全（Transport Layer Security，TLS）连接所需的全部密码学原语。

**安全存储（Secure Storage）**：API 提供与存储加密有关的全部原语，适用于块存储或文件存储；主加密密钥（Master Encryption Key）保存在密钥存储区（Key Store）中。

**网络凭据（Network Credentials）**：API 支持在密钥存储区内管理网络凭据，例如企业网络中基于 X.509 的认证或预共享密钥（Pre-shared Key）。

**设备配对（Device Pairing）**：API 支持通常用于无线设备安全配对的密钥协商协议（Key Agreement Protocol）。例如，近场通信（Near Field Communication，NFC）令牌或蓝牙设备首次使用时，可以通过密钥协商协议完成配对。

**安全启动（Secure Boot）**：API 提供在安全启动或可信启动过程中验证固件完整性（Integrity）和真实性（Authenticity）的原语。

**证明（Attestation）**：API 提供证明操作使用的原语。这里的证明能力是指设备用设备私钥对字节数组签名，并将结果返回给调用方。用途包括证明设备状态，以及生成密钥对并证明该密钥对是在安全密钥存储区内部生成的。API 提供常用于这些证明操作的算法。

**工厂预配（Factory Provisioning）**：大多数物联网（Internet of Things，IoT）设备会在工厂预配过程中，或者部署到现场之后，获得唯一身份。此 API 提供向设备写入代表该身份的密钥所需的接口。

## 3.4\_使用注意事项（Usage Considerations）

### 始终检查错误（Always Check for Errors）

PSA Crypto API 中的大多数函数都可能返回错误。所有可能失败的函数均以 `psa_status_t` 为返回类型。少数不会失败的函数则返回 `void` 或其他类型。

发生错误后，除非另有说明，否则输出参数的内容未定义，不得使用。

常见错误原因包括：

- 如果密钥的存储和处理环境与应用所在环境相互分离，所有需要访问密码处理环境的函数，都可能因两个环境间的通信错误而失败。
- 如果算法由逻辑上独立于应用处理器的硬件加速器实现，即使应用处理器仍正常运行，加速器也可能发生故障。
- 大多数函数都可能因资源不足而失败。不过，某些实现保证特定函数始终具有足够内存。
- 所有访问持久密钥（Persistent Key）的函数都可能因存储故障而失败。
- 所有需要随机性的函数都可能因熵（Entropy）不足而失败。建议实现在执行 `psa_crypto_init()` 时，用足够的熵为随机数生成器设置种子。但某些安全标准要求定期从硬件随机数生成器重新获取种子，此过程也可能失败。

### 共享内存与并发（Shared Memory and Concurrency）

有的环境支持多线程应用，有的环境不支持。有的环境允许应用与不同的安全上下文（Security Context）共享内存。在多线程应用或共享内存环境中，编写应用时必须注意避免数据损坏或泄露；本规范要求应用遵守相应约束。

一般而言，对于任何给定对象，PSA Crypto API 允许一个写入者，或任意数量的并发读取者。也就是说，如果两个或更多调用同时访问同一对象，只有所有调用都只读取该对象而不修改它时，其行为才有明确定义。读取访问既包括通过输入参数读取内存，也包括使用密钥时读取密钥存储区内容。详情参阅[并发调用（Concurrent Calls）](https://arm-software.github.io/psa-api/crypto/1.2/overview/conventions.html#concurrent-calls)。

如果应用与另一个安全上下文共享内存，可以将共享内存块作为输入缓冲区或输出缓冲区传入，但不能作为非缓冲区参数（Non-buffer Parameters）传入。详情参阅[参数稳定性（Stability of Parameters）](https://arm-software.github.io/psa-api/crypto/1.2/overview/conventions.html#stability-of-parameters)。

### 使用后清理（Cleaning Up after Use）

为尽量减少系统遭到攻破时的影响，建议应用在敏感数据不再使用时，将其从内存中擦除。这样可能泄露的就只有当前正在使用的数据，而过去的数据不会因此暴露。

敏感数据清理包括：

- 清除栈（Stack）或堆（Heap）上的临时缓冲区。
- 中止不会继续完成的操作。
- 销毁不再使用的密钥。

## 3.5\_参考资料（References）

- [PSA Crypto 官方规范](https://arm-software.github.io/psa-api/crypto/)。
- [Mbed TLS 项目](https://www.trustedfirmware.org/projects/mbed-tls/)。

译注：上述内容说明 PSA 接口的设计和约定，具体硬件与后端支持的算法、密钥存储能力仍须按当前构建核对。本集的[随机数指南](../data_utilities/P006_随机数生成.md)、[内部可信存储示例](P006_PSA内部可信存储示例.md)与[持久密钥示例](P007_PSA持久密钥示例.md)可配合阅读。


<a id="psa-crypto"></a>
<a id="id1"></a>
<a id="overview"></a>
<a id="design-goals"></a>
<a id="examples-of-applications"></a>
<a id="usage-considerations"></a>
<a id="references"></a>

<!-- reading-navigation:start -->

**主线阅读**

[上一篇：密码学接口指南](P002_密码学接口指南.md) · [本模块主线目录](../reading/crypto.md) · [全部主线](../reading/README.md) · [下一篇：JSONWebToken指南](P029_JSONWebToken指南.md)

<details>
<summary>原册编号导航（含扩展参考）</summary>

[上一章](P002_密码学接口指南.md) · [返回大纲](大纲.md) · [下一章](P004_密码驱动测试示例.md)

</details>

<!-- reading-navigation:end -->
