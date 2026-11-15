---
id: learning.zephyr-docs.kconfig-reference.page-318
title: "`subsys/authentication`配置项参考"
kind: reference
status: evolving
domains: [zephyr, kconfig, configuration]
source_url: https://docs.zephyrproject.org/latest/kconfig.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；分册、相对路径和明确标注的译注为本地新增。 -->

# 第318章\_`subsys/authentication`配置项参考

本章翻译官方 Kconfig 数据库中 `subsys/authentication` 的 41 条定义记录。提示（Prompt）、帮助（Help）与菜单路径均已翻译；条件表达式和配置标识符保持原样，默认值除有译注明示的构建机路径相对化外保留原值。原页：[Kconfig Search](https://docs.zephyrproject.org/latest/kconfig.html)。来源数据库版本为 `main`，快照摘要与完整覆盖范围见[本册大纲](大纲.md)。

`main` 源码链接随上游变化；行号来自本次数据库快照，不能视为固定提交定位。无提示的配置项保留其不可直接由用户赋值的属性。原库中存在未收录定义的交叉引用，本章在对应位置明确标出。

<a id="CONFIG_FIDO2"></a>

## 318.1 `CONFIG_FIDO2`

**提示（Prompt）**：FIDO2 身份验证器（FIDO2 authenticator）

**说明（Help）**

启用 FIDO2/CTAP2 身份验证器子系统（authenticator subsystem）。

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_ZCBOR
CONFIG_ZCBOR_CANONICAL
CONFIG_PSA_CRYPTO
CONFIG_SECURE_STORAGE if !CONFIG_BUILD_WITH_TFM
CONFIG_PSA_WANT_KEY_TYPE_ECC_KEY_PAIR_GENERATE
CONFIG_PSA_WANT_KEY_TYPE_ECC_PUBLIC_KEY
CONFIG_PSA_WANT_ALG_ECDSA
CONFIG_PSA_WANT_ALG_ECDH
CONFIG_PSA_WANT_ALG_SHA_256
CONFIG_PSA_WANT_ALG_GCM
CONFIG_PSA_WANT_ALG_HMAC
CONFIG_PSA_WANT_ALG_CBC_NO_PADDING
CONFIG_PSA_WANT_ECC_SECP_R1_256
```

**定义位置（Location）**：[`subsys/authentication/fido2/Kconfig:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/authentication/fido2/Kconfig#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 身份认证（Authentication）

**配置项引用（Symbol References）**：[`CONFIG_ZCBOR`](P254_modules_zcbor_配置项参考.md#CONFIG_ZCBOR)、[`CONFIG_ZCBOR_CANONICAL`](P254_modules_zcbor_配置项参考.md#CONFIG_ZCBOR_CANONICAL)、[`CONFIG_PSA_CRYPTO`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_CRYPTO)、[`CONFIG_SECURE_STORAGE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SECURE_STORAGE)、[`CONFIG_BUILD_WITH_TFM`](P252_modules_trusted-firmware-m_配置项参考.md#CONFIG_BUILD_WITH_TFM)、[`CONFIG_PSA_WANT_KEY_TYPE_ECC_KEY_PAIR_GENERATE`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_WANT_KEY_TYPE_ECC_KEY_PAIR_GENERATE)、[`CONFIG_PSA_WANT_KEY_TYPE_ECC_PUBLIC_KEY`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_WANT_KEY_TYPE_ECC_PUBLIC_KEY)、[`CONFIG_PSA_WANT_ALG_ECDSA`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_WANT_ALG_ECDSA)、[`CONFIG_PSA_WANT_ALG_ECDH`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_WANT_ALG_ECDH)、[`CONFIG_PSA_WANT_ALG_SHA_256`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_WANT_ALG_SHA_256)、[`CONFIG_PSA_WANT_ALG_GCM`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_WANT_ALG_GCM)、[`CONFIG_PSA_WANT_ALG_HMAC`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_WANT_ALG_HMAC)、[`CONFIG_PSA_WANT_ALG_CBC_NO_PADDING`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_WANT_ALG_CBC_NO_PADDING)、[`CONFIG_PSA_WANT_ECC_SECP_R1_256`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_WANT_ECC_SECP_R1_256)。

<a id="CONFIG_FIDO2_AAGUID"></a>

## 318.2 `CONFIG_FIDO2_AAGUID`

**提示（Prompt）**：身份验证器 AAGUID（Authenticator AAGUID，32 个十六进制字符）

**说明（Help）**

将身份验证器 AAGUID 编码为 32 个十六进制字符，不含分隔符（共 16 字节）。

**类型（Type）**：字符串（String），`string`。

**依赖条件（Dependencies）**

```text
CONFIG_FIDO2
```

**定义位置（Location）**：[`subsys/authentication/fido2/Kconfig:87`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/authentication/fido2/Kconfig#L87)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 身份认证（Authentication） → FIDO2 身份验证器（FIDO2 authenticator）

**配置项引用（Symbol References）**：[`CONFIG_FIDO2`](P318_subsys_authentication_配置项参考.md#CONFIG_FIDO2)。

<a id="CONFIG_FIDO2_ALWAYS_UV"></a>

## 318.3 `CONFIG_FIDO2_ALWAYS_UV`

**提示（Prompt）**：始终要求用户验证（Always require user verification）

**说明（Help）**

启用后，每次 `MakeCredential` 和 `GetAssertion` 操作都强制进行用户验证（user verification），无论依赖方（Relying Party）如何请求；即使 `userVerification` 设为 `"discouraged"` 也如此。本设置覆盖 `makeCredUvNotRqd`。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_FIDO2
```

**定义位置（Location）**：[`subsys/authentication/fido2/Kconfig:93`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/authentication/fido2/Kconfig#L93)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 身份认证（Authentication） → FIDO2 身份验证器（FIDO2 authenticator）

**配置项引用（Symbol References）**：[`CONFIG_FIDO2`](P318_subsys_authentication_配置项参考.md#CONFIG_FIDO2)。

<a id="CONFIG_FIDO2_ATTESTATION_BACKEND"></a>

## 318.4 `CONFIG_FIDO2_ATTESTATION_BACKEND`

**提示（Prompt）**：认证证明后端（Attestation backend）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_FIDO2
```

**默认值（Defaults）**

```text
CONFIG_FIDO2_ATTESTATION_SELF
```

**可选项（Choices）**

```text
CONFIG_FIDO2_ATTESTATION_SELF
CONFIG_FIDO2_ATTESTATION_CUSTOM
CONFIG_FIDO2_ATTESTATION_NONE
```

**定义位置（Location）**：[`subsys/authentication/fido2/attestation/Kconfig:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/authentication/fido2/attestation/Kconfig#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 身份认证（Authentication） → FIDO2 身份验证器（FIDO2 authenticator） → 认证证明（Attestation）

**配置项引用（Symbol References）**：[`CONFIG_FIDO2`](P318_subsys_authentication_配置项参考.md#CONFIG_FIDO2)、[`CONFIG_FIDO2_ATTESTATION_SELF`](P318_subsys_authentication_配置项参考.md#CONFIG_FIDO2_ATTESTATION_SELF)、[`CONFIG_FIDO2_ATTESTATION_CUSTOM`](P318_subsys_authentication_配置项参考.md#CONFIG_FIDO2_ATTESTATION_CUSTOM)、[`CONFIG_FIDO2_ATTESTATION_NONE`](P318_subsys_authentication_配置项参考.md#CONFIG_FIDO2_ATTESTATION_NONE)。

<a id="CONFIG_FIDO2_ATTESTATION_CUSTOM"></a>

## 318.5 `CONFIG_FIDO2_ATTESTATION_CUSTOM`

**提示（Prompt）**：自定义，由应用提供（Custom, application-provided）

**说明（Help）**

使用自定义认证证明后端（custom attestation backend），身份验证器（authenticator）使用应用提供的密钥或证书生成认证证明（attestation）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_FIDO2_ATTESTATION_BACKEND>
```

**定义位置（Location）**：[`subsys/authentication/fido2/attestation/Kconfig:16`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/authentication/fido2/attestation/Kconfig#L16)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 身份认证（Authentication） → FIDO2 身份验证器（FIDO2 authenticator） → 认证证明（Attestation） → 认证证明后端（Attestation backend）

**配置项引用（Symbol References）**：[`CONFIG_FIDO2_ATTESTATION_BACKEND`](P318_subsys_authentication_配置项参考.md#CONFIG_FIDO2_ATTESTATION_BACKEND)。

<a id="CONFIG_FIDO2_ATTESTATION_NONE"></a>

## 318.6 `CONFIG_FIDO2_ATTESTATION_NONE`

**提示（Prompt）**：无（None）

**说明（Help）**

不提供任何认证证明（attestation）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_FIDO2_ATTESTATION_BACKEND>
```

**定义位置（Location）**：[`subsys/authentication/fido2/attestation/Kconfig:22`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/authentication/fido2/attestation/Kconfig#L22)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 身份认证（Authentication） → FIDO2 身份验证器（FIDO2 authenticator） → 认证证明（Attestation） → 认证证明后端（Attestation backend）

**配置项引用（Symbol References）**：[`CONFIG_FIDO2_ATTESTATION_BACKEND`](P318_subsys_authentication_配置项参考.md#CONFIG_FIDO2_ATTESTATION_BACKEND)。

<a id="CONFIG_FIDO2_ATTESTATION_SELF"></a>

## 318.7 `CONFIG_FIDO2_ATTESTATION_SELF`

**提示（Prompt）**：自证明，使用 packed 格式与凭据密钥（Self, packed, credential key）

**说明（Help）**

使用自证明（self attestation）。这是最简单的认证证明（attestation）形式，不需要额外的密钥或证书。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_FIDO2_ATTESTATION_BACKEND>
```

**定义位置（Location）**：[`subsys/authentication/fido2/attestation/Kconfig:10`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/authentication/fido2/attestation/Kconfig#L10)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 身份认证（Authentication） → FIDO2 身份验证器（FIDO2 authenticator） → 认证证明（Attestation） → 认证证明后端（Attestation backend）

**配置项引用（Symbol References）**：[`CONFIG_FIDO2_ATTESTATION_BACKEND`](P318_subsys_authentication_配置项参考.md#CONFIG_FIDO2_ATTESTATION_BACKEND)。

<a id="CONFIG_FIDO2_BLE_CONTROL_POINT_LENGTH"></a>

## 318.8 `CONFIG_FIDO2_BLE_CONTROL_POINT_LENGTH`

**提示（Prompt）**：FIDO 控制点最大写入长度（Maximum FIDO Control Point write length）

**说明（Help）**

通过低功耗蓝牙（Bluetooth LE）单次写入 FIDO 控制点特征（FIDO Control Point characteristic）的最大大小，单位为字节。大于 `20` 的值要求协商出相应较大的 ATT 最大传输单元（ATT MTU），并提供相应大小的蓝牙缓冲区（Bluetooth buffers）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_FIDO2_TRANSPORT_BLE && CONFIG_FIDO2
```

**默认值（Defaults）**

```text
20
```

**取值范围（Ranges）**

```text
[20, 512]
```

**定义位置（Location）**：[`subsys/authentication/fido2/transport/Kconfig:72`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/authentication/fido2/transport/Kconfig#L72)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 身份认证（Authentication） → FIDO2 身份验证器（FIDO2 authenticator） → 传输（Transport） → 基于低功耗蓝牙的 CTAP（CTAP over Bluetooth LE）

**配置项引用（Symbol References）**：[`CONFIG_FIDO2_TRANSPORT_BLE`](P318_subsys_authentication_配置项参考.md#CONFIG_FIDO2_TRANSPORT_BLE)、[`CONFIG_FIDO2`](P318_subsys_authentication_配置项参考.md#CONFIG_FIDO2)。

<a id="CONFIG_FIDO2_BLE_KEEPALIVE_INTERVAL_MS"></a>

## 318.9 `CONFIG_FIDO2_BLE_KEEPALIVE_INTERVAL_MS`

**提示（Prompt）**：FIDO2 低功耗蓝牙保活间隔（FIDO2 Bluetooth LE keepalive interval）

**说明（Help）**

身份验证器（authenticator）处理请求或等待用户在场（user presence）时，发送 `KEEPALIVE` 通知的请求间隔，单位为毫秒。定时器周期至少等于有效的低功耗蓝牙连接间隔（Bluetooth LE connection interval），其中包括外设延迟（peripheral latency）；连接参数发生变化时，此周期也会调整。最大值和默认值均对应 CTAP 低功耗蓝牙中的 `kKeepAliveMillis` 值，即 `500` 毫秒。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_FIDO2_TRANSPORT_BLE && CONFIG_FIDO2
```

**默认值（Defaults）**

```text
500
```

**取值范围（Ranges）**

```text
[10, 500]
```

**定义位置（Location）**：[`subsys/authentication/fido2/transport/Kconfig:96`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/authentication/fido2/transport/Kconfig#L96)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 身份认证（Authentication） → FIDO2 身份验证器（FIDO2 authenticator） → 传输（Transport） → 基于低功耗蓝牙的 CTAP（CTAP over Bluetooth LE）

**配置项引用（Symbol References）**：[`CONFIG_FIDO2_TRANSPORT_BLE`](P318_subsys_authentication_配置项参考.md#CONFIG_FIDO2_TRANSPORT_BLE)、[`CONFIG_FIDO2`](P318_subsys_authentication_配置项参考.md#CONFIG_FIDO2)。

<a id="CONFIG_FIDO2_BLE_REQUIRE_AUTHENTICATED_LINK"></a>

## 318.10 `CONFIG_FIDO2_BLE_REQUIRE_AUTHENTICATED_LINK`

**提示（Prompt）**：要求经过身份认证的低功耗蓝牙配对（authenticated Bluetooth LE pairing）

**说明（Help）**

要求蓝牙安全级别 3（Bluetooth Security Level 3），而非最低的加密安全级别 2（encrypted Security Level 2）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_FIDO2_TRANSPORT_BLE && CONFIG_FIDO2
```

**定义位置（Location）**：[`subsys/authentication/fido2/transport/Kconfig:58`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/authentication/fido2/transport/Kconfig#L58)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 身份认证（Authentication） → FIDO2 身份验证器（FIDO2 authenticator） → 传输（Transport） → 基于低功耗蓝牙的 CTAP（CTAP over Bluetooth LE）

**配置项引用（Symbol References）**：[`CONFIG_FIDO2_TRANSPORT_BLE`](P318_subsys_authentication_配置项参考.md#CONFIG_FIDO2_TRANSPORT_BLE)、[`CONFIG_FIDO2`](P318_subsys_authentication_配置项参考.md#CONFIG_FIDO2)。

<a id="CONFIG_FIDO2_BLE_RX_QUEUE_DEPTH"></a>

## 318.11 `CONFIG_FIDO2_BLE_RX_QUEUE_DEPTH`

**提示（Prompt）**：低功耗蓝牙接收队列深度（Receive Bluetooth LE queue depth）

**说明（Help）**

能够排队等待处理的控制点分片（Control Point fragments）数量。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_FIDO2_TRANSPORT_BLE && CONFIG_FIDO2
```

**默认值（Defaults）**

```text
8
```

**取值范围（Ranges）**

```text
[1, 32]
```

**定义位置（Location）**：[`subsys/authentication/fido2/transport/Kconfig:81`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/authentication/fido2/transport/Kconfig#L81)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 身份认证（Authentication） → FIDO2 身份验证器（FIDO2 authenticator） → 传输（Transport） → 基于低功耗蓝牙的 CTAP（CTAP over Bluetooth LE）

**配置项引用（Symbol References）**：[`CONFIG_FIDO2_TRANSPORT_BLE`](P318_subsys_authentication_配置项参考.md#CONFIG_FIDO2_TRANSPORT_BLE)、[`CONFIG_FIDO2`](P318_subsys_authentication_配置项参考.md#CONFIG_FIDO2)。

<a id="CONFIG_FIDO2_BLE_RX_TIMEOUT_MS"></a>

## 318.12 `CONFIG_FIDO2_BLE_RX_TIMEOUT_MS`

**提示（Prompt）**：RX 重组超时，单位为毫秒（RX reassembly timeout）

**说明（Help）**

对于尚未完整接收的 FIDO 低功耗蓝牙消息（FIDO Bluetooth LE message），等待下一个分片（fragment）的最短时间，单位为毫秒。有效超时时间至少等于当前低功耗蓝牙连接间隔（Bluetooth LE connection interval）。默认值对应 CTAP 低功耗蓝牙的 `kMaxCommandTransmitDelayMillis` 值。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_FIDO2_TRANSPORT_BLE && CONFIG_FIDO2
```

**默认值（Defaults）**

```text
1500
```

**取值范围（Ranges）**

```text
[1500, 10000]
```

**定义位置（Location）**：[`subsys/authentication/fido2/transport/Kconfig:110`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/authentication/fido2/transport/Kconfig#L110)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 身份认证（Authentication） → FIDO2 身份验证器（FIDO2 authenticator） → 传输（Transport） → 基于低功耗蓝牙的 CTAP（CTAP over Bluetooth LE）

**配置项引用（Symbol References）**：[`CONFIG_FIDO2_TRANSPORT_BLE`](P318_subsys_authentication_配置项参考.md#CONFIG_FIDO2_TRANSPORT_BLE)、[`CONFIG_FIDO2`](P318_subsys_authentication_配置项参考.md#CONFIG_FIDO2)。

<a id="CONFIG_FIDO2_BLE_RX_WORKQ_STACK_SIZE"></a>

## 318.13 `CONFIG_FIDO2_BLE_RX_WORKQ_STACK_SIZE`

**提示（Prompt）**：低功耗蓝牙 RX 工作队列栈大小（Bluetooth LE RX workqueue stack size）

**说明（Help）**

用于处理传入 FIDO 低功耗蓝牙分片（FIDO Bluetooth LE fragments）的专用蓝牙接收工作队列（RX workqueue）的栈大小。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_FIDO2_TRANSPORT_BLE && CONFIG_FIDO2
```

**默认值（Defaults）**

```text
4096
```

**取值范围（Ranges）**

```text
[1024, 16384]
```

**定义位置（Location）**：[`subsys/authentication/fido2/transport/Kconfig:64`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/authentication/fido2/transport/Kconfig#L64)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 身份认证（Authentication） → FIDO2 身份验证器（FIDO2 authenticator） → 传输（Transport） → 基于低功耗蓝牙的 CTAP（CTAP over Bluetooth LE）

**配置项引用（Symbol References）**：[`CONFIG_FIDO2_TRANSPORT_BLE`](P318_subsys_authentication_配置项参考.md#CONFIG_FIDO2_TRANSPORT_BLE)、[`CONFIG_FIDO2`](P318_subsys_authentication_配置项参考.md#CONFIG_FIDO2)。

<a id="CONFIG_FIDO2_BLE_TX_FRAME_COUNT"></a>

## 318.14 `CONFIG_FIDO2_BLE_TX_FRAME_COUNT`

**提示（Prompt）**：FIDO 低功耗蓝牙发送帧数（FIDO Bluetooth LE transmit frame count）

**说明（Help）**

可排入队列、通过低功耗蓝牙（Bluetooth LE）异步发送的完整 FIDO 帧（frames）数量。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_FIDO2_TRANSPORT_BLE && CONFIG_FIDO2
```

**默认值（Defaults）**

```text
4
```

**取值范围（Ranges）**

```text
[2, 8]
```

**定义位置（Location）**：[`subsys/authentication/fido2/transport/Kconfig:88`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/authentication/fido2/transport/Kconfig#L88)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 身份认证（Authentication） → FIDO2 身份验证器（FIDO2 authenticator） → 传输（Transport） → 基于低功耗蓝牙的 CTAP（CTAP over Bluetooth LE）

**配置项引用（Symbol References）**：[`CONFIG_FIDO2_TRANSPORT_BLE`](P318_subsys_authentication_配置项参考.md#CONFIG_FIDO2_TRANSPORT_BLE)、[`CONFIG_FIDO2`](P318_subsys_authentication_配置项参考.md#CONFIG_FIDO2)。

<a id="CONFIG_FIDO2_CBOR_MAX_SIZE"></a>

## 318.15 `CONFIG_FIDO2_CBOR_MAX_SIZE`

**提示（Prompt）**：CBOR 消息缓冲区最大大小（Maximum CBOR message buffer size）

**说明（Help）**

采用 CBOR 编码的 CTAP2 请求与响应消息（request and response messages）的最大大小。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_FIDO2
```

**默认值（Defaults）**

```text
1024
```

**取值范围（Ranges）**

```text
[1024, 4096]
```

**定义位置（Location）**：[`subsys/authentication/fido2/Kconfig:36`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/authentication/fido2/Kconfig#L36)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 身份认证（Authentication） → FIDO2 身份验证器（FIDO2 authenticator）

**配置项引用（Symbol References）**：[`CONFIG_FIDO2`](P318_subsys_authentication_配置项参考.md#CONFIG_FIDO2)。

<a id="CONFIG_FIDO2_CREDENTIAL_MANAGEMENT"></a>

## 318.16 `CONFIG_FIDO2_CREDENTIAL_MANAGEMENT`

**提示（Prompt）**：凭据管理命令（Credential management command）

**说明（Help）**

启用 CTAP 2.1 的 `authenticatorCredentialManagement`（`0x0A`）命令。需要 PIN 协议（PIN protocol）支持，因为所有 `credMgmt` 子命令都需要具有 CM 权限的 `pinUvAuthToken`。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_FIDO2
```

**定义位置（Location）**：[`subsys/authentication/fido2/Kconfig:80`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/authentication/fido2/Kconfig#L80)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 身份认证（Authentication） → FIDO2 身份验证器（FIDO2 authenticator）

**配置项引用（Symbol References）**：[`CONFIG_FIDO2`](P318_subsys_authentication_配置项参考.md#CONFIG_FIDO2)。

<a id="CONFIG_FIDO2_CTAPHID_KEEPALIVE_INTERVAL_MS"></a>

## 318.17 `CONFIG_FIDO2_CTAPHID_KEEPALIVE_INTERVAL_MS`

**提示（Prompt）**：CTAPHID 保活间隔，单位为毫秒（CTAPHID keepalive interval）

**说明（Help）**

CTAPHID 保活数据包（keepalive packets）的间隔。对于 USB HID，规范要求该值不得超过 `100ms`，以免主机超时（host timeouts）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_FIDO2_TRANSPORT_USB_HID && CONFIG_FIDO2
```

**默认值（Defaults）**

```text
100
```

**取值范围（Ranges）**

```text
[20, 100]
```

**定义位置（Location）**：[`subsys/authentication/fido2/transport/Kconfig:24`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/authentication/fido2/transport/Kconfig#L24)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 身份认证（Authentication） → FIDO2 身份验证器（FIDO2 authenticator） → 传输（Transport） → 基于 USB HID 的 CTAP（CTAP over USB HID）

**配置项引用（Symbol References）**：[`CONFIG_FIDO2_TRANSPORT_USB_HID`](P318_subsys_authentication_配置项参考.md#CONFIG_FIDO2_TRANSPORT_USB_HID)、[`CONFIG_FIDO2`](P318_subsys_authentication_配置项参考.md#CONFIG_FIDO2)。

<a id="CONFIG_FIDO2_CTAPHID_TIMEOUT_MS"></a>

## 318.18 `CONFIG_FIDO2_CTAPHID_TIMEOUT_MS`

**提示（Prompt）**：CTAPHID 消息重组超时，单位为毫秒（CTAPHID message reassembly timeout）

**说明（Help）**

CTAPHID 消息重组（message reassembly）期间等待后续数据包（continuation packets）的最长时间。如果超时前未收到完整消息，身份验证器（authenticator）将发送错误响应并中止事务（transaction）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_FIDO2_TRANSPORT_USB_HID && CONFIG_FIDO2
```

**默认值（Defaults）**

```text
1000
```

**取值范围（Ranges）**

```text
[100, 2000]
```

**定义位置（Location）**：[`subsys/authentication/fido2/transport/Kconfig:13`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/authentication/fido2/transport/Kconfig#L13)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 身份认证（Authentication） → FIDO2 身份验证器（FIDO2 authenticator） → 传输（Transport） → 基于 USB HID 的 CTAP（CTAP over USB HID）

**配置项引用（Symbol References）**：[`CONFIG_FIDO2_TRANSPORT_USB_HID`](P318_subsys_authentication_配置项参考.md#CONFIG_FIDO2_TRANSPORT_USB_HID)、[`CONFIG_FIDO2`](P318_subsys_authentication_配置项参考.md#CONFIG_FIDO2)。

<a id="CONFIG_FIDO2_EXT_CRED_BLOB"></a>

## 318.19 `CONFIG_FIDO2_EXT_CRED_BLOB`

**提示（Prompt）**：credBlob 扩展（credBlob extension）

**说明（Help）**

启用 CTAP2 的 `credBlob` 扩展（extension）。需要 `credProtect` 支持。支持 `credBlob` 的身份验证器（authenticators）也必须（MUST）支持 `credProtect`。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_FIDO2_EXT_CRED_PROTECT && CONFIG_FIDO2
```

**定义位置（Location）**：[`subsys/authentication/fido2/Kconfig:68`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/authentication/fido2/Kconfig#L68)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 身份认证（Authentication） → FIDO2 身份验证器（FIDO2 authenticator）

**配置项引用（Symbol References）**：[`CONFIG_FIDO2_EXT_CRED_PROTECT`](P318_subsys_authentication_配置项参考.md#CONFIG_FIDO2_EXT_CRED_PROTECT)、[`CONFIG_FIDO2`](P318_subsys_authentication_配置项参考.md#CONFIG_FIDO2)。

<a id="CONFIG_FIDO2_EXT_CRED_PROTECT"></a>

## 318.20 `CONFIG_FIDO2_EXT_CRED_PROTECT`

**提示（Prompt）**：credProtect 扩展（credProtect extension）

**说明（Help）**

启用 CTAP2 的 `credProtect` 扩展（extension）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_FIDO2
```

**定义位置（Location）**：[`subsys/authentication/fido2/Kconfig:51`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/authentication/fido2/Kconfig#L51)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 身份认证（Authentication） → FIDO2 身份验证器（FIDO2 authenticator）

**配置项引用（Symbol References）**：[`CONFIG_FIDO2`](P318_subsys_authentication_配置项参考.md#CONFIG_FIDO2)。

<a id="CONFIG_FIDO2_EXT_HMAC_SECRET"></a>

## 318.21 `CONFIG_FIDO2_EXT_HMAC_SECRET`

**提示（Prompt）**：hmac-secret 扩展（hmac-secret extension）

**说明（Help）**

启用 CTAP2 的 `hmac-secret` 扩展（extension）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_FIDO2
```

**主动选择（Selects）**

```text
CONFIG_PSA_WANT_ALG_HMAC
```

**定义位置（Location）**：[`subsys/authentication/fido2/Kconfig:56`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/authentication/fido2/Kconfig#L56)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 身份认证（Authentication） → FIDO2 身份验证器（FIDO2 authenticator）

**配置项引用（Symbol References）**：[`CONFIG_FIDO2`](P318_subsys_authentication_配置项参考.md#CONFIG_FIDO2)、[`CONFIG_PSA_WANT_ALG_HMAC`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_WANT_ALG_HMAC)。

<a id="CONFIG_FIDO2_EXT_LARGE_BLOB_KEY"></a>

## 318.22 `CONFIG_FIDO2_EXT_LARGE_BLOB_KEY`

**提示（Prompt）**：largeBlobKey 扩展（largeBlobKey extension）

**说明（Help）**

启用 CTAP2 的 `largeBlobKey` 扩展（extension），为每条凭据提供大数据块存储（per-credential large blob storage）。本快照中尚未实现。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_FIDO2
```

**定义位置（Location）**：[`subsys/authentication/fido2/Kconfig:62`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/authentication/fido2/Kconfig#L62)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 身份认证（Authentication） → FIDO2 身份验证器（FIDO2 authenticator）

**配置项引用（Symbol References）**：[`CONFIG_FIDO2`](P318_subsys_authentication_配置项参考.md#CONFIG_FIDO2)。

<a id="CONFIG_FIDO2_EXT_THIRD_PARTY_PAYMENT"></a>

## 318.23 `CONFIG_FIDO2_EXT_THIRD_PARTY_PAYMENT`

**提示（Prompt）**：thirdPartyPayment 扩展（thirdPartyPayment extension）

**说明（Help）**

启用 CTAP2 的 `thirdPartyPayment` 扩展（extension）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_FIDO2
```

**定义位置（Location）**：[`subsys/authentication/fido2/Kconfig:75`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/authentication/fido2/Kconfig#L75)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 身份认证（Authentication） → FIDO2 身份验证器（FIDO2 authenticator）

**配置项引用（Symbol References）**：[`CONFIG_FIDO2`](P318_subsys_authentication_配置项参考.md#CONFIG_FIDO2)。

<a id="CONFIG_FIDO2_HID_RX_WORKQ_STACK_SIZE"></a>

## 318.24 `CONFIG_FIDO2_HID_RX_WORKQ_STACK_SIZE`

**提示（Prompt）**：USB HID RX 工作队列栈大小（USB HID RX workqueue stack size）

**说明（Help）**

用于处理传入 CTAPHID 报告（reports）的专用 USB HID 接收工作队列（RX workqueue）的栈大小。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_FIDO2_TRANSPORT_USB_HID && CONFIG_FIDO2
```

**默认值（Defaults）**

```text
4096
```

**取值范围（Ranges）**

```text
[1024, 16384]
```

**定义位置（Location）**：[`subsys/authentication/fido2/transport/Kconfig:33`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/authentication/fido2/transport/Kconfig#L33)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 身份认证（Authentication） → FIDO2 身份验证器（FIDO2 authenticator） → 传输（Transport） → 基于 USB HID 的 CTAP（CTAP over USB HID）

**配置项引用（Symbol References）**：[`CONFIG_FIDO2_TRANSPORT_USB_HID`](P318_subsys_authentication_配置项参考.md#CONFIG_FIDO2_TRANSPORT_USB_HID)、[`CONFIG_FIDO2`](P318_subsys_authentication_配置项参考.md#CONFIG_FIDO2)。

<a id="CONFIG_FIDO2_MAX_CREDENTIALS"></a>

## 318.25 `CONFIG_FIDO2_MAX_CREDENTIALS`

**提示（Prompt）**：驻留凭据最大数量（Maximum number of resident credentials）

**说明（Help）**

可存储在设备上的可发现凭据（discoverable credentials），即驻留凭据（resident credentials）的最大数量。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_FIDO2
```

**默认值（Defaults）**

```text
16
```

**取值范围（Ranges）**

```text
[1, 256]
```

**定义位置（Location）**：[`subsys/authentication/fido2/Kconfig:43`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/authentication/fido2/Kconfig#L43)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 身份认证（Authentication） → FIDO2 身份验证器（FIDO2 authenticator）

**配置项引用（Symbol References）**：[`CONFIG_FIDO2`](P318_subsys_authentication_配置项参考.md#CONFIG_FIDO2)。

<a id="CONFIG_FIDO2_MIN_PIN_LENGTH"></a>

## 318.26 `CONFIG_FIDO2_MIN_PIN_LENGTH`

**提示（Prompt）**：PIN 最小长度（Minimum PIN length）

**说明（Help）**

身份验证器（authenticator）强制要求的 PIN 最小长度（minimum PIN length）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_FIDO2
```

**默认值（Defaults）**

```text
4
```

**取值范围（Ranges）**

```text
[4, 63]
```

**定义位置（Location）**：[`subsys/authentication/fido2/Kconfig:110`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/authentication/fido2/Kconfig#L110)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 身份认证（Authentication） → FIDO2 身份验证器（FIDO2 authenticator）

**配置项引用（Symbol References）**：[`CONFIG_FIDO2`](P318_subsys_authentication_配置项参考.md#CONFIG_FIDO2)。

<a id="CONFIG_FIDO2_PIN_MAX_RETRIES"></a>

## 318.27 `CONFIG_FIDO2_PIN_MAX_RETRIES`

**提示（Prompt）**：锁定前的最大 PIN 重试次数（Maximum PIN retries before lockout）

**说明（Help）**

PIN 被禁用前剩余的最大尝试次数。根据 CTAP2 规范，该值不得超过 `8`。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_FIDO2
```

**默认值（Defaults）**

```text
8
```

**取值范围（Ranges）**

```text
[1, 8]
```

**定义位置（Location）**：[`subsys/authentication/fido2/Kconfig:102`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/authentication/fido2/Kconfig#L102)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 身份认证（Authentication） → FIDO2 身份验证器（FIDO2 authenticator）

**配置项引用（Symbol References）**：[`CONFIG_FIDO2`](P318_subsys_authentication_配置项参考.md#CONFIG_FIDO2)。

<a id="CONFIG_FIDO2_PIN_TOKEN_TIMEOUT_MS"></a>

## 318.28 `CONFIG_FIDO2_PIN_TOKEN_TIMEOUT_MS`

**提示（Prompt）**：pinUvAuthToken 使用超时，单位为毫秒（usage timeout, ms）

**说明（Help）**

`pinUvAuthToken` 保持有效的最长时间，单位为毫秒。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_FIDO2
```

**默认值（Defaults）**

```text
30000
```

**定义位置（Location）**：[`subsys/authentication/fido2/Kconfig:117`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/authentication/fido2/Kconfig#L117)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 身份认证（Authentication） → FIDO2 身份验证器（FIDO2 authenticator）

**配置项引用（Symbol References）**：[`CONFIG_FIDO2`](P318_subsys_authentication_配置项参考.md#CONFIG_FIDO2)。

<a id="CONFIG_FIDO2_STORAGE_BACKEND"></a>

## 318.29 `CONFIG_FIDO2_STORAGE_BACKEND`

**提示（Prompt）**：凭据存储后端（Credential storage backend）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_FIDO2
```

**默认值（Defaults）**

```text
CONFIG_FIDO2_STORAGE_SETTINGS
```

**可选项（Choices）**

```text
CONFIG_FIDO2_STORAGE_SETTINGS
CONFIG_FIDO2_STORAGE_NONE
CONFIG_FIDO2_STORAGE_CUSTOM
```

**定义位置（Location）**：[`subsys/authentication/fido2/storage/Kconfig:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/authentication/fido2/storage/Kconfig#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 身份认证（Authentication） → FIDO2 身份验证器（FIDO2 authenticator） → 凭据存储（Credential Storage）

**配置项引用（Symbol References）**：[`CONFIG_FIDO2`](P318_subsys_authentication_配置项参考.md#CONFIG_FIDO2)、[`CONFIG_FIDO2_STORAGE_SETTINGS`](P318_subsys_authentication_配置项参考.md#CONFIG_FIDO2_STORAGE_SETTINGS)、[`CONFIG_FIDO2_STORAGE_NONE`](P318_subsys_authentication_配置项参考.md#CONFIG_FIDO2_STORAGE_NONE)、[`CONFIG_FIDO2_STORAGE_CUSTOM`](P318_subsys_authentication_配置项参考.md#CONFIG_FIDO2_STORAGE_CUSTOM)。

<a id="CONFIG_FIDO2_STORAGE_CUSTOM"></a>

## 318.30 `CONFIG_FIDO2_STORAGE_CUSTOM`

**提示（Prompt）**：自定义，由应用提供（Custom, application-provided）

**说明（Help）**

不从该子系统编译任何存储后端（storage backend）。应用程序必须提供自己的实现。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_FIDO2_STORAGE_BACKEND>
```

**定义位置（Location）**：[`subsys/authentication/fido2/storage/Kconfig:22`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/authentication/fido2/storage/Kconfig#L22)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 身份认证（Authentication） → FIDO2 身份验证器（FIDO2 authenticator） → 凭据存储（Credential Storage） → 凭据存储后端（Credential storage backend）

**配置项引用（Symbol References）**：[`CONFIG_FIDO2_STORAGE_BACKEND`](P318_subsys_authentication_配置项参考.md#CONFIG_FIDO2_STORAGE_BACKEND)。

<a id="CONFIG_FIDO2_STORAGE_NONE"></a>

## 318.31 `CONFIG_FIDO2_STORAGE_NONE`

**提示（Prompt）**：无持久化存储（No persistent storage）

**说明（Help）**

设备上不存储任何凭据（credentials）。适用于只签发不可发现凭据（non-discoverable credentials）的情况。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_FIDO2_STORAGE_BACKEND>
```

**定义位置（Location）**：[`subsys/authentication/fido2/storage/Kconfig:16`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/authentication/fido2/storage/Kconfig#L16)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 身份认证（Authentication） → FIDO2 身份验证器（FIDO2 authenticator） → 凭据存储（Credential Storage） → 凭据存储后端（Credential storage backend）

**配置项引用（Symbol References）**：[`CONFIG_FIDO2_STORAGE_BACKEND`](P318_subsys_authentication_配置项参考.md#CONFIG_FIDO2_STORAGE_BACKEND)。

<a id="CONFIG_FIDO2_STORAGE_SETTINGS"></a>

## 318.32 `CONFIG_FIDO2_STORAGE_SETTINGS`

**提示（Prompt）**：Zephyr 设置子系统（Zephyr settings subsystem）

**说明（Help）**

使用 Zephyr 设置子系统（settings subsystem）存储 FIDO2 凭据（credentials）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SETTINGS && <choice CONFIG_FIDO2_STORAGE_BACKEND>
```

**定义位置（Location）**：[`subsys/authentication/fido2/storage/Kconfig:10`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/authentication/fido2/storage/Kconfig#L10)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 身份认证（Authentication） → FIDO2 身份验证器（FIDO2 authenticator） → 凭据存储（Credential Storage） → 凭据存储后端（Credential storage backend）

**配置项引用（Symbol References）**：[`CONFIG_SETTINGS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SETTINGS)、[`CONFIG_FIDO2_STORAGE_BACKEND`](P318_subsys_authentication_配置项参考.md#CONFIG_FIDO2_STORAGE_BACKEND)。

<a id="CONFIG_FIDO2_THREAD_PRIORITY"></a>

## 318.33 `CONFIG_FIDO2_THREAD_PRIORITY`

**提示（Prompt）**：FIDO2 处理线程优先级（FIDO2 processing thread priority）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_FIDO2
```

**默认值（Defaults）**

```text
7
```

**定义位置（Location）**：[`subsys/authentication/fido2/Kconfig:32`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/authentication/fido2/Kconfig#L32)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 身份认证（Authentication） → FIDO2 身份验证器（FIDO2 authenticator）

**配置项引用（Symbol References）**：[`CONFIG_FIDO2`](P318_subsys_authentication_配置项参考.md#CONFIG_FIDO2)。

<a id="CONFIG_FIDO2_THREAD_STACK_SIZE"></a>

## 318.34 `CONFIG_FIDO2_THREAD_STACK_SIZE`

**提示（Prompt）**：FIDO2 处理线程栈大小（FIDO2 processing thread stack size）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_FIDO2
```

**默认值（Defaults）**

```text
4096
```

**定义位置（Location）**：[`subsys/authentication/fido2/Kconfig:28`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/authentication/fido2/Kconfig#L28)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 身份认证（Authentication） → FIDO2 身份验证器（FIDO2 authenticator）

**配置项引用（Symbol References）**：[`CONFIG_FIDO2`](P318_subsys_authentication_配置项参考.md#CONFIG_FIDO2)。

<a id="CONFIG_FIDO2_TRANSPORT_BLE"></a>

## 318.35 `CONFIG_FIDO2_TRANSPORT_BLE`

**提示（Prompt）**：基于低功耗蓝牙的 CTAP（CTAP over Bluetooth LE）

**说明（Help）**

启用通过低功耗蓝牙（Bluetooth LE）进行的 FIDO2 通信（CTAP）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_PERIPHERAL && CONFIG_BT_GATT_ENFORCE_SUBSCRIPTION && CONFIG_BT_SMP && CONFIG_BT_DIS && CONFIG_BT_DIS_MANUF_NAME && CONFIG_BT_DIS_MODEL_NUMBER && CONFIG_BT_DIS_FW_REV && CONFIG_BT_BONDING_REQUIRED && CONFIG_BT_USER_CONN_PARAM_REJECTED && CONFIG_FIDO2
```

**定义位置（Location）**：[`subsys/authentication/fido2/transport/Kconfig:42`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/authentication/fido2/transport/Kconfig#L42)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 身份认证（Authentication） → FIDO2 身份验证器（FIDO2 authenticator） → 传输（Transport）

**配置项引用（Symbol References）**：[`CONFIG_BT_PERIPHERAL`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT_PERIPHERAL)、[`CONFIG_BT_GATT_ENFORCE_SUBSCRIPTION`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_GATT_ENFORCE_SUBSCRIPTION)、[`CONFIG_BT_SMP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_SMP)、[`CONFIG_BT_DIS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_DIS)、[`CONFIG_BT_DIS_MANUF_NAME`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_DIS_MANUF_NAME)、[`CONFIG_BT_DIS_MODEL_NUMBER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_DIS_MODEL_NUMBER)、[`CONFIG_BT_DIS_FW_REV`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_DIS_FW_REV)、[`CONFIG_BT_BONDING_REQUIRED`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_BONDING_REQUIRED)、[`CONFIG_BT_USER_CONN_PARAM_REJECTED`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_USER_CONN_PARAM_REJECTED)、[`CONFIG_FIDO2`](P318_subsys_authentication_配置项参考.md#CONFIG_FIDO2)。

<a id="CONFIG_FIDO2_TRANSPORT_USB_HID"></a>

## 318.36 `CONFIG_FIDO2_TRANSPORT_USB_HID`

**提示（Prompt）**：基于 USB HID 的 CTAP（CTAP over USB HID）

**说明（Help）**

启用通过 USB HID 进行的 FIDO2 通信（CTAPHID）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_USB_DEVICE_STACK_NEXT && CONFIG_FIDO2
```

**主动选择（Selects）**

```text
CONFIG_USBD_HID_SUPPORT
```

**定义位置（Location）**：[`subsys/authentication/fido2/transport/Kconfig:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/authentication/fido2/transport/Kconfig#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 身份认证（Authentication） → FIDO2 身份验证器（FIDO2 authenticator） → 传输（Transport）

**配置项引用（Symbol References）**：[`CONFIG_USB_DEVICE_STACK_NEXT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USB_DEVICE_STACK_NEXT)、[`CONFIG_FIDO2`](P318_subsys_authentication_配置项参考.md#CONFIG_FIDO2)、[`CONFIG_USBD_HID_SUPPORT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USBD_HID_SUPPORT)。

<a id="CONFIG_FIDO2_UP_ALWAYS"></a>

## 318.37 `CONFIG_FIDO2_UP_ALWAYS`

**提示（Prompt）**：始终批准（Always approve）

**说明（Help）**

绕过用户在场检查（user presence）并始终返回成功。这会降低安全性，只应在测试或十分特定的使用场景中采用。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_FIDO2_UP_BACKEND>
```

**主动选择（Selects）**

```text
CONFIG_NOT_SECURE
```

**定义位置（Location）**：[`subsys/authentication/fido2/up/Kconfig:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/authentication/fido2/up/Kconfig#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 身份认证（Authentication） → FIDO2 身份验证器（FIDO2 authenticator） → 用户在场（User Presence） → 用户在场后端（User presence backend）

**配置项引用（Symbol References）**：[`CONFIG_FIDO2_UP_BACKEND`](P318_subsys_authentication_配置项参考.md#CONFIG_FIDO2_UP_BACKEND)、[`CONFIG_NOT_SECURE`](P003_Kconfig.zephyr_配置项参考_1.md#CONFIG_NOT_SECURE)。

<a id="CONFIG_FIDO2_UP_BACKEND"></a>

## 318.38 `CONFIG_FIDO2_UP_BACKEND`

**提示（Prompt）**：用户在场后端（User presence backend）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_FIDO2
```

**默认值（Defaults）**

```text
CONFIG_FIDO2_UP_INPUT
```

**可选项（Choices）**

```text
CONFIG_FIDO2_UP_INPUT
CONFIG_FIDO2_UP_ALWAYS
CONFIG_FIDO2_UP_CUSTOM
```

**定义位置（Location）**：[`subsys/authentication/fido2/up/Kconfig:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/authentication/fido2/up/Kconfig#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 身份认证（Authentication） → FIDO2 身份验证器（FIDO2 authenticator） → 用户在场（User Presence）

**配置项引用（Symbol References）**：[`CONFIG_FIDO2`](P318_subsys_authentication_配置项参考.md#CONFIG_FIDO2)、[`CONFIG_FIDO2_UP_INPUT`](P318_subsys_authentication_配置项参考.md#CONFIG_FIDO2_UP_INPUT)、[`CONFIG_FIDO2_UP_ALWAYS`](P318_subsys_authentication_配置项参考.md#CONFIG_FIDO2_UP_ALWAYS)、[`CONFIG_FIDO2_UP_CUSTOM`](P318_subsys_authentication_配置项参考.md#CONFIG_FIDO2_UP_CUSTOM)。

<a id="CONFIG_FIDO2_UP_CUSTOM"></a>

## 318.39 `CONFIG_FIDO2_UP_CUSTOM`

**提示（Prompt）**：自定义，由应用提供（Custom, application-provided）

**说明（Help）**

不从该子系统编译任何用户在场来源（UP source）。应用程序必须提供自己的实现。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_FIDO2_UP_BACKEND>
```

**定义位置（Location）**：[`subsys/authentication/fido2/up/Kconfig:24`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/authentication/fido2/up/Kconfig#L24)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 身份认证（Authentication） → FIDO2 身份验证器（FIDO2 authenticator） → 用户在场（User Presence） → 用户在场后端（User presence backend）

**配置项引用（Symbol References）**：[`CONFIG_FIDO2_UP_BACKEND`](P318_subsys_authentication_配置项参考.md#CONFIG_FIDO2_UP_BACKEND)。

<a id="CONFIG_FIDO2_UP_INPUT"></a>

## 318.40 `CONFIG_FIDO2_UP_INPUT`

**提示（Prompt）**：输入设备（Input device）

**说明（Help）**

使用输入子系统（INPUT subsystem）检查用户在场（user presence）。采用设备树 chosen 属性（devicetree chosen property）`zephyr,fido2-up-input`。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_INPUT && <choice CONFIG_FIDO2_UP_BACKEND>
```

**定义位置（Location）**：[`subsys/authentication/fido2/up/Kconfig:10`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/authentication/fido2/up/Kconfig#L10)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 身份认证（Authentication） → FIDO2 身份验证器（FIDO2 authenticator） → 用户在场（User Presence） → 用户在场后端（User presence backend）

**配置项引用（Symbol References）**：[`CONFIG_INPUT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_INPUT)、[`CONFIG_FIDO2_UP_BACKEND`](P318_subsys_authentication_配置项参考.md#CONFIG_FIDO2_UP_BACKEND)。

<a id="CONFIG_FIDO2_UP_TIMEOUT_MS"></a>

## 318.41 `CONFIG_FIDO2_UP_TIMEOUT_MS`

**提示（Prompt）**：用户在场超时，单位为毫秒（User presence timeout）

**说明（Help）**

等待用户在场确认（user presence confirmation）的超时时间。根据 FIDO2 规范，默认值为 `30` 秒。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_FIDO2
```

**默认值（Defaults）**

```text
30000
```

**定义位置（Location）**：[`subsys/authentication/fido2/up/Kconfig:32`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/authentication/fido2/up/Kconfig#L32)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 身份认证（Authentication） → FIDO2 身份验证器（FIDO2 authenticator） → 用户在场（User Presence）

**配置项引用（Symbol References）**：[`CONFIG_FIDO2`](P318_subsys_authentication_配置项参考.md#CONFIG_FIDO2)。

<!-- kconfig-navigation -->

[上一章](P317_subsys_Kconfig_配置项参考.md) · [返回大纲](大纲.md) · [下一章](P319_subsys_bindesc_配置项参考.md)
