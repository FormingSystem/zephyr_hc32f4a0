---
id: learning.zephyr-docs.services-overview.page-4
title: FIDO2认证器
kind: reference
status: maintained
domains: [zephyr, services, documentation]
source_url: https://docs.zephyrproject.org/latest/services/authentication/fido2/index.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->


<a id="fido2-authenticator"></a>
<a id="fido2-api"></a>

# 第4章\_FIDO2认证器

原文：[官方页面](https://docs.zephyrproject.org/latest/services/authentication/fido2/index.html)。读取日期：2026-10-14；保存的 latest 页面及 HTML 摘要见[来源记录](../SOURCES.md)。


<a id="overview"></a>

## 4.1\_概览（Overview）

FIDO2 认证器子系统实现 [FIDO2 客户端到认证器协议（Client to Authenticator Protocol，CTAP2）规范](https://fidoalliance.org/specs/fido-v2.2-rd-20230321/fido-client-to-authenticator-protocol-v2.2-rd-20230321.html)，使 Zephyr 设备可用作无密码认证（passwordless authentication）的硬件安全密钥。通过 [`CONFIG_FIDO2`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_FIDO2) 启用该子系统。

FIDO2 安全密钥配合 [WebAuthn 网页认证标准](https://www.w3.org/TR/webauthn-2/)使用。依赖方（relying party），即网站或服务，通过浏览器或操作系统平台这样的客户端与认证器交互，注册并验证使用者凭据。认证器使用保存在设备上的密钥执行密码操作，密钥不会离开硬件。

当前支持以下 CTAP2 命令：

- `authenticatorMakeCredential`：创建凭据。
- `authenticatorGetAssertion`：取得认证断言。
- `authenticatorGetInfo`：取得认证器信息。
- `authenticatorClientPIN`：客户端 PIN 相关操作。
- `authenticatorGetNextAssertion`：取得下一条认证断言。
- `authenticatorSelection`：认证器选择。


<a id="architecture"></a>

## 4.2\_架构（Architecture）

子系统组织为可插拔后端组件，在构建时通过 Kconfig 选择。

### 4.2.1\_传输（Transport）

负责主机与认证器之间的线路协议通信。传输通过 [`FIDO2_TRANSPORT_DEFINE`](https://docs.zephyrproject.org/latest/doxygen/html/fido2__transport_8h.html#a146a5108012a6b5092458cc1e14340c8) 注册，启动时遍历。可选传输为：

- USB 人机接口设备（Human Interface Device，HID）传输 CTAPHID：[`CONFIG_FIDO2_TRANSPORT_USB_HID`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_FIDO2_TRANSPORT_USB_HID)。
- 蓝牙低功耗（Bluetooth Low Energy，Bluetooth LE）传输 CTAPBLE：[`CONFIG_FIDO2_TRANSPORT_BLE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_FIDO2_TRANSPORT_BLE)。

### 4.2.2\_使用者在场（User Presence，UP）

确认确实有人在设备旁操作。通过 [`CONFIG_FIDO2_UP_BACKEND`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_FIDO2_UP_BACKEND) 选择后端：

- 输入设备：[`CONFIG_FIDO2_UP_INPUT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_FIDO2_UP_INPUT)。
- 始终批准：[`CONFIG_FIDO2_UP_ALWAYS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_FIDO2_UP_ALWAYS)。
- 应用提供的自定义实现：[`CONFIG_FIDO2_UP_CUSTOM`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_FIDO2_UP_CUSTOM)。

### 4.2.3\_凭据存储（Credential Storage）

持久保存可发现的凭据（discoverable credential），也称驻留凭据（resident credential）。通过 [`CONFIG_FIDO2_STORAGE_BACKEND`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_FIDO2_STORAGE_BACKEND) 选择：

- Settings 设置子系统：[`CONFIG_FIDO2_STORAGE_SETTINGS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_FIDO2_STORAGE_SETTINGS)。
- 不使用存储：[`CONFIG_FIDO2_STORAGE_NONE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_FIDO2_STORAGE_NONE)，仅支持不可发现凭据。

### 4.2.4\_证明（Attestation）

为新创建的凭据签名以证明其来源。通过 [`CONFIG_FIDO2_ATTESTATION_BACKEND`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_FIDO2_ATTESTATION_BACKEND) 选择：

- 自证明（self attestation）：[`CONFIG_FIDO2_ATTESTATION_SELF`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_FIDO2_ATTESTATION_SELF)，默认选项。
- 不提供证明：[`CONFIG_FIDO2_ATTESTATION_NONE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_FIDO2_ATTESTATION_NONE)。
- 应用提供的自定义证明：[`CONFIG_FIDO2_ATTESTATION_CUSTOM`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_FIDO2_ATTESTATION_CUSTOM)。


<a id="usage"></a>

## 4.3\_使用方法（Usage）

使用子系统时，包含主头文件：

```c
#include <zephyr/authentication/fido2/fido2.h>
```


<a id="basic-initialization"></a>

### 4.3.1\_基本初始化（Basic Initialization）

认证器要与主机通信，至少必须启用一种传输。完整初始化顺序见 [FIDO2 认证器示例](../basic_samples/P057_FIDO2认证器示例.md#fido2)。


<a id="runtime-state-monitoring"></a>

### 4.3.2\_运行时状态监测（Runtime State Monitoring）

子系统提供运行时状态回调（runtime state callback），应用可据此驱动 LED 等状态指示器：

```c
#include <zephyr/authentication/fido2/fido2.h>

static void on_state_change(enum fido2_runtime_state state, void *user_data)
{
    switch (state) {
    case FIDO2_RUNTIME_STATE_IDLE:
        /* LED off */
        break;
    case FIDO2_RUNTIME_STATE_WAITING_USER_PRESENCE:
        /* Blink LED */
        break;
    case FIDO2_RUNTIME_STATE_PROCESSING:
        /* LED on solid */
        break;
    default:
        break;
    }
}

fido2_set_state_callback(on_state_change, NULL);
```

原例注释译文：空闲状态 `FIDO2_RUNTIME_STATE_IDLE` 时关闭 LED；等待使用者在场的 `FIDO2_RUNTIME_STATE_WAITING_USER_PRESENCE` 状态让 LED 闪烁；处理状态 `FIDO2_RUNTIME_STATE_PROCESSING` 时让 LED 常亮。


<a id="extensions"></a>

## 4.4\_扩展（Extensions）

CTAP2 扩展尚未实现。以下 Kconfig 选项为未来实现预留：

| 扩展 | 配置选项 |
| --- | --- |
| `credProtect` | [`CONFIG_FIDO2_EXT_CRED_PROTECT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_FIDO2_EXT_CRED_PROTECT) |
| `hmac-secret` | [`CONFIG_FIDO2_EXT_HMAC_SECRET`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_FIDO2_EXT_HMAC_SECRET) |
| `largeBlobKey` | [`CONFIG_FIDO2_EXT_LARGE_BLOB_KEY`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_FIDO2_EXT_LARGE_BLOB_KEY) |
| `credBlob` | [`CONFIG_FIDO2_EXT_CRED_BLOB`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_FIDO2_EXT_CRED_BLOB) |
| `thirdPartyPayment` | [`CONFIG_FIDO2_EXT_THIRD_PARTY_PAYMENT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_FIDO2_EXT_THIRD_PARTY_PAYMENT) |


<a id="references"></a>

## 4.5\_参考资料（References）

- [FIDO2 CTAP2 规范](https://fidoalliance.org/specs/fido-v2.2-rd-20230321/fido-client-to-authenticator-protocol-v2.2-rd-20230321.html)。
- [WebAuthn 规范](https://www.w3.org/TR/webauthn-2/)。
- [FIDO 联盟（FIDO Alliance）](https://fidoalliance.org/)。


<a id="api-reference"></a>

## 4.6\_API与相关示例（API Reference / Related Code Samples）

接口参考：[FIDO2 API](https://docs.zephyrproject.org/latest/doxygen/html/group__fido2.html)。

[FIDO2 认证器示例](../basic_samples/P057_FIDO2认证器示例.md#fido2)：实现 FIDO2/CTAP2 硬件安全密钥。


对应官方文档源码：[doc/services/authentication/fido2/index.rst](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/doc/services/authentication/fido2/index.rst)。

> 译注——源码跟踪：本仓库的[对应源码](../../../doc/services/authentication/fido2/index.rst)可用于跟踪，版本可能与网页不同；本批仅翻译和核对文档，没有执行固件构建、模拟运行或烧录。

<!-- reading-navigation:start -->

**主线阅读**

[上一篇：身份认证入口](P003_身份认证入口.md) · [本模块主线目录](../reading/services_overview.md) · [全部主线](../reading/README.md) · [下一篇：连接服务入口](P005_连接服务入口.md)

<details>
<summary>原册编号导航（含扩展参考）</summary>

[上一章](P003_身份认证入口.md) · [返回大纲](大纲.md) · [下一章](P005_连接服务入口.md)

</details>

<!-- reading-navigation:end -->
