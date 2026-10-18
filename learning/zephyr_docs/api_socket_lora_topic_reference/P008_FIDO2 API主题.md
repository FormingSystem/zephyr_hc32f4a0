---
id: learning.zephyr-docs.api-socket-lora-topic-reference.page-8
title: FIDO2 API主题
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__fido2.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第8章\_FIDO2 API主题

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__fido2.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

FIDO2 身份认证器子系统（Authenticator subsystem）。

<a id="details"></a>

FIDO2 认证器子系统（Authenticator Subsystem）。起始版本（Since）：4.5。版本（Version）：0.1.1。

<a id="header-files"></a>
<a id="files"></a>

## 8.1\_文件（Files）

<a id="r_fido2_2Eh"></a>

```c
file fido2.h
```

相关声明：[fido2.h](../api_file_service_interface_reference/P020_zephyr__authentication__fido2__fido2.h_文件参考.md)。

FIDO2认证器（Authenticator）的公共API。

<a id="r_fido2_5Fattestation_2Eh"></a>

```c
file fido2_attestation.h
```

相关声明：[fido2_attestation.h](../api_file_service_reference/P013_zephyr__authentication__fido2__fido2_attestation.h_文件参考.md)。

FIDO2证明回调（Attestation Callback）的API。

<a id="r_fido2_5Fstorage_2Eh"></a>

```c
file fido2_storage.h
```

相关声明：[fido2_storage.h](../api_file_configuration_reference/P027_zephyr__authentication__fido2__fido2_storage.h_文件参考.md)。

FIDO2凭据存储（Credential Storage）的API。

<a id="r_fido2_5Ftransport_2Eh"></a>

```c
file fido2_transport.h
```

相关声明：[fido2_transport.h](../api_file_secure_value_reference/P008_zephyr__authentication__fido2__fido2_transport.h_文件参考.md)。

FIDO2传输抽象（Transport Abstraction）的API。

<a id="r_fido2_5Ftypes_2Eh"></a>

```c
file fido2_types.h
```

相关声明：[fido2_types.h](../api_file_flash_test_reference/P002_zephyr__authentication__fido2__fido2_types.h_文件参考.md)。

FIDO2共享类型定义（Shared Type Definitions）。

<a id="r_fido2_5Fup_2Eh"></a>

```c
file fido2_up.h
```

相关声明：[fido2_up.h](../api_file_runtime_reference/P015_zephyr__authentication__fido2__fido2_up.h_文件参考.md)。

FIDO2用户在场（User Presence）抽象API。

<a id="header-typedef-members"></a>
<a id="typedef-members"></a>

## 8.2\_类型定义（Typedefs）

<a id="r_gad0a191f4a48998fe857dc6315d225d94"></a>

```c
typedef void(* fido2_state_callback_t) (enum fido2_runtime_state state, void *user_data)
```

相关声明：[fido2_state_callback_t](#gad0a191f4a48998fe857dc6315d225d94)、[fido2_runtime_state](#gabf5068079e94310fb4b942df56ec1d10)、[state](../api_file_reference/P291_zephyr__net__http__parser_state.h_文件参考.md#adc6e5733fc3c22f0a7b2914188c49c90)。

FIDO2 运行时状态回调（Runtime State Callback）。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 8.3\_枚举（Enumerations）

<a id="r_gabf5068079e94310fb4b942df56ec1d10"></a>

```c
enum fido2_runtime_state { FIDO2_RUNTIME_STATE_STOPPED = 0 , FIDO2_RUNTIME_STATE_IDLE , FIDO2_RUNTIME_STATE_WAITING_USER_PRESENCE , FIDO2_RUNTIME_STATE_PROCESSING }
```

相关声明：[fido2_runtime_state](#gabf5068079e94310fb4b942df56ec1d10)、[FIDO2_RUNTIME_STATE_STOPPED](#ggabf5068079e94310fb4b942df56ec1d10acc12ded1d9bd2a04d4b6346c186f8a67)、[FIDO2_RUNTIME_STATE_IDLE](#ggabf5068079e94310fb4b942df56ec1d10a8c7700d3df270e15fc9e6cd0a536bd9a)、[FIDO2_RUNTIME_STATE_WAITING_USER_PRESENCE](#ggabf5068079e94310fb4b942df56ec1d10ac1dcd5cc47e59480df023bcc6d239909)、[FIDO2_RUNTIME_STATE_PROCESSING](#ggabf5068079e94310fb4b942df56ec1d10a64e677309cf5594b723f9b5c76e52774)。

FIDO2 子系统对外提供的运行时状态（Runtime States）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 8.4\_函数（Functions）

<a id="r_ga020303d5fcc00471feba64eec8e169c2"></a>

```c
int fido2_init (void)
```

相关声明：[fido2_init](#ga020303d5fcc00471feba64eec8e169c2)。

初始化 FIDO2 子系统（Subsystem）。

<a id="r_gae7a1b8c0bf42ee2a0c3de0bc54c4fa72"></a>

```c
int fido2_start (void)
```

相关声明：[fido2_start](#gae7a1b8c0bf42ee2a0c3de0bc54c4fa72)。

启动 FIDO2 认证器（Authenticator）。

<a id="r_gab41b4d957882b8d6844316ec2f3ccc95"></a>

```c
int fido2_stop (void)
```

相关声明：[fido2_stop](#gab41b4d957882b8d6844316ec2f3ccc95)。

停止 FIDO2 认证器（Authenticator）。

<a id="r_gac2fecd9d7d18fbb8ff4b8e1083f86059"></a>

```c
int fido2_set_state_callback (fido2_state_callback_t cb, void *user_data)
```

相关声明：[fido2_set_state_callback](#gac2fecd9d7d18fbb8ff4b8e1083f86059)、[fido2_state_callback_t](#gad0a191f4a48998fe857dc6315d225d94)。

设置或清除唯一的 FIDO2 运行时状态回调（Runtime State Callback）。

<a id="r_gaeb4e348615069d77a81fb87c6970b640"></a>

```c
enum fido2_runtime_state fido2_get_state (void)
```

相关声明：[fido2_runtime_state](#gabf5068079e94310fb4b942df56ec1d10)、[fido2_get_state](#gaeb4e348615069d77a81fb87c6970b640)。

获取 FIDO2 当前运行时状态（Runtime State）。

<a id="r_gaeb569aaa63c3c005d0df0b08c38896e1"></a>

```c
int fido2_reset (void)
```

相关声明：[fido2_reset](#gaeb569aaa63c3c005d0df0b08c38896e1)。

执行恢复出厂设置（Factory Reset）。

<a id="r_ga6b3b79c7ef54b3ebbe686d4f67aaf7fc"></a>

```c
enum fido2_status { FIDO2_OK = 0x00 , FIDO2_ERR_INVALID_COMMAND = 0x01 , FIDO2_ERR_INVALID_PARAMETER = 0x02 , FIDO2_ERR_INVALID_LENGTH = 0x03 , FIDO2_ERR_INVALID_SEQ = 0x04 , FIDO2_ERR_TIMEOUT = 0x05 , FIDO2_ERR_CHANNEL_BUSY = 0x06 , FIDO2_ERR_LOCK_REQUIRED = 0x0A , FIDO2_ERR_INVALID_CHANNEL = 0x0B , FIDO2_ERR_CBOR_UNEXPECTED_TYPE = 0x11 , FIDO2_ERR_INVALID_CBOR = 0x12 , FIDO2_ERR_MISSING_PARAMETER = 0x14 , FIDO2_ERR_LIMIT_EXCEEDED = 0x15 , FIDO2_ERR_UNSUPPORTED_EXTENSION = 0x16 , FIDO2_ERR_FP_DATABASE_FULL = 0x17 , FIDO2_ERR_LARGE_BLOB_STORAGE_FULL = 0x18 , FIDO2_ERR_CREDENTIAL_EXCLUDED = 0x19 , FIDO2_ERR_PROCESSING = 0x21 , FIDO2_ERR_INVALID_CREDENTIAL = 0x22 , FIDO2_ERR_USER_ACTION_PENDING = 0x23 , FIDO2_ERR_OPERATION_PENDING = 0x24 , FIDO2_ERR_NO_OPERATIONS = 0x25 , FIDO2_ERR_UNSUPPORTED_ALGORITHM = 0x26 , FIDO2_ERR_OPERATION_DENIED = 0x27 , FIDO2_ERR_KEY_STORE_FULL = 0x28 , FIDO2_ERR_UNSUPPORTED_OPTION = 0x2B , FIDO2_ERR_INVALID_OPTION = 0x2C , FIDO2_ERR_KEEPALIVE_CANCEL = 0x2D , FIDO2_ERR_NO_CREDENTIALS = 0x2E , FIDO2_ERR_USER_ACTION_TIMEOUT = 0x2F , FIDO2_ERR_NOT_ALLOWED = 0x30 , FIDO2_ERR_PIN_INVALID = 0x31 , FIDO2_ERR_PIN_BLOCKED = 0x32 , FIDO2_ERR_PIN_AUTH_INVALID = 0x33 , FIDO2_ERR_PIN_AUTH_BLOCKED = 0x34 , FIDO2_ERR_PIN_NOT_SET = 0x35 , FIDO2_ERR_PUAT_REQUIRED = 0x36 , FIDO2_ERR_PIN_POLICY_VIOLATION = 0x37 , FIDO2_ERR_RESERVED = 0x38 , FIDO2_ERR_REQUEST_TOO_LARGE = 0x39 , FIDO2_ERR_ACTION_TIMEOUT = 0x3A , FIDO2_ERR_UP_REQUIRED = 0x3B , FIDO2_ERR_UV_BLOCKED = 0x3C , FIDO2_ERR_INTEGRITY_FAILURE = 0x3D , FIDO2_ERR_INVALID_SUBCOMMAND = 0x3E , FIDO2_ERR_UV_INVALID = 0x3F , FIDO2_ERR_UNAUTHORIZED_PERMISSION = 0x40 , FIDO2_ERR_OTHER = 0x7F }
```

相关声明：[fido2_status](#ga6b3b79c7ef54b3ebbe686d4f67aaf7fc)、[FIDO2_OK](#ga6b3b79c7ef54b3ebbe686d4f67aaf7fcaa08efc6dee799b3e1fb8490bc64bd1cf)、[FIDO2_ERR_INVALID_COMMAND](#ga6b3b79c7ef54b3ebbe686d4f67aaf7fcab263ae4a933b875d54a86d4a6da8dc4e)、[FIDO2_ERR_INVALID_PARAMETER](#ga6b3b79c7ef54b3ebbe686d4f67aaf7fcab4382a900e27d13b5043241f2f6dc2fe)、[FIDO2_ERR_INVALID_LENGTH](#ga6b3b79c7ef54b3ebbe686d4f67aaf7fcacbaf6656b7eac960f4bc0e561de47011)、[FIDO2_ERR_INVALID_SEQ](#ga6b3b79c7ef54b3ebbe686d4f67aaf7fca809431ef12cd0ba7094a80c39d6bdc2d)、[FIDO2_ERR_TIMEOUT](#ga6b3b79c7ef54b3ebbe686d4f67aaf7fcaf713403e6582ce02cace5d29f45405af)、[FIDO2_ERR_CHANNEL_BUSY](#ga6b3b79c7ef54b3ebbe686d4f67aaf7fcac36b384a558597d72980f2425008c7b6)、[FIDO2_ERR_LOCK_REQUIRED](#ga6b3b79c7ef54b3ebbe686d4f67aaf7fcacf7163e857eb9b8b6ddef1e7ff2b7351)、[FIDO2_ERR_INVALID_CHANNEL](#ga6b3b79c7ef54b3ebbe686d4f67aaf7fca1ece48887496a5962823530201eaf48c)、[FIDO2_ERR_CBOR_UNEXPECTED_TYPE](#ga6b3b79c7ef54b3ebbe686d4f67aaf7fca17c4a70a8f87425c4d849585d28280d4)、[FIDO2_ERR_INVALID_CBOR](#ga6b3b79c7ef54b3ebbe686d4f67aaf7fcac804a5a070c6552d89d403ffc953c00d)、[FIDO2_ERR_MISSING_PARAMETER](#ga6b3b79c7ef54b3ebbe686d4f67aaf7fcad19e5127b17b8e0abee8bfe7d1ae595f)、[FIDO2_ERR_LIMIT_EXCEEDED](#ga6b3b79c7ef54b3ebbe686d4f67aaf7fcaee29e086a2af8e697b6467c9667cb327)、[FIDO2_ERR_UNSUPPORTED_EXTENSION](#ga6b3b79c7ef54b3ebbe686d4f67aaf7fcabe9d8c984a0c0a62616a4a94af655a78)、[FIDO2_ERR_FP_DATABASE_FULL](#ga6b3b79c7ef54b3ebbe686d4f67aaf7fcacc4208f8ab39ba6b67c9358df6b88797)、[FIDO2_ERR_LARGE_BLOB_STORAGE_FULL](#ga6b3b79c7ef54b3ebbe686d4f67aaf7fcaffdba1168067976851629c2111f46f6a)、[FIDO2_ERR_CREDENTIAL_EXCLUDED](#ga6b3b79c7ef54b3ebbe686d4f67aaf7fca5dfe38f41a7863bc04928d7c566568b7)、[FIDO2_ERR_PROCESSING](#ga6b3b79c7ef54b3ebbe686d4f67aaf7fca128911647928193e076041834e398e75)、[FIDO2_ERR_INVALID_CREDENTIAL](#ga6b3b79c7ef54b3ebbe686d4f67aaf7fca4c53af9f0ad3e857bf86efea60b9370f)、[FIDO2_ERR_USER_ACTION_PENDING](#ga6b3b79c7ef54b3ebbe686d4f67aaf7fca8d108ee70faea78aa0669a90081dd05c)、[FIDO2_ERR_OPERATION_PENDING](#ga6b3b79c7ef54b3ebbe686d4f67aaf7fca020a5895146a35c2dedace5e0ff96112)、[FIDO2_ERR_NO_OPERATIONS](#ga6b3b79c7ef54b3ebbe686d4f67aaf7fca376b899ff97c4d39f201f20e03a36ed7)、[FIDO2_ERR_UNSUPPORTED_ALGORITHM](#ga6b3b79c7ef54b3ebbe686d4f67aaf7fca3521d75934cddcd0d009279541381c41)、[FIDO2_ERR_OPERATION_DENIED](#ga6b3b79c7ef54b3ebbe686d4f67aaf7fca507f5ded749fdba95d6b16d859052d43)、[FIDO2_ERR_KEY_STORE_FULL](#ga6b3b79c7ef54b3ebbe686d4f67aaf7fcacb6d4da143bbd72b7d361a7a4e38b1da)、[FIDO2_ERR_UNSUPPORTED_OPTION](#ga6b3b79c7ef54b3ebbe686d4f67aaf7fcaad5b849ccb37209d531444bb346e3158)、[FIDO2_ERR_INVALID_OPTION](#ga6b3b79c7ef54b3ebbe686d4f67aaf7fca05bb5e1370a3e46ef1a2f2545cf5675c)、[FIDO2_ERR_KEEPALIVE_CANCEL](#ga6b3b79c7ef54b3ebbe686d4f67aaf7fca336c3e439e0a1b3eb24cf3edc38455e1)、[FIDO2_ERR_NO_CREDENTIALS](#ga6b3b79c7ef54b3ebbe686d4f67aaf7fcafcbd15f2df2744ed0afd3613540ad6a3)、[FIDO2_ERR_USER_ACTION_TIMEOUT](#ga6b3b79c7ef54b3ebbe686d4f67aaf7fca39355da927952f311dd8cdf9fe5cced8)、[FIDO2_ERR_NOT_ALLOWED](#ga6b3b79c7ef54b3ebbe686d4f67aaf7fca739a74cd005fc1b3b8853f7aa2db7e3e)、[FIDO2_ERR_PIN_INVALID](#ga6b3b79c7ef54b3ebbe686d4f67aaf7fca6eb4c3a5f51db1d0232ef8ca21d194e6)、[FIDO2_ERR_PIN_BLOCKED](#ga6b3b79c7ef54b3ebbe686d4f67aaf7fca05c0bff840ed8b7e85c147876792760f)、[FIDO2_ERR_PIN_AUTH_INVALID](#ga6b3b79c7ef54b3ebbe686d4f67aaf7fca63548371fe576d03e00a2d428bf2501b)、[FIDO2_ERR_PIN_AUTH_BLOCKED](#ga6b3b79c7ef54b3ebbe686d4f67aaf7fca57a9754a770796bdb303ec5503222060)、[FIDO2_ERR_PIN_NOT_SET](#ga6b3b79c7ef54b3ebbe686d4f67aaf7fcab59eee02a04da8ca4bf54ceba81794d0)、[FIDO2_ERR_PUAT_REQUIRED](#ga6b3b79c7ef54b3ebbe686d4f67aaf7fca5c952ab01843550e24d3aa672f05fec9)、[FIDO2_ERR_PIN_POLICY_VIOLATION](#ga6b3b79c7ef54b3ebbe686d4f67aaf7fca8406e112b928b9f556cced2f0c391cfe)、[FIDO2_ERR_RESERVED](#ga6b3b79c7ef54b3ebbe686d4f67aaf7fca935a727495553c4bf584a92c39d780b7)、[FIDO2_ERR_REQUEST_TOO_LARGE](#ga6b3b79c7ef54b3ebbe686d4f67aaf7fca0ca1a5d18e501d446c58ddcc4f8fbc05)、[FIDO2_ERR_ACTION_TIMEOUT](#ga6b3b79c7ef54b3ebbe686d4f67aaf7fca356a92621e9d79fd5d599f1c13a7da93)、[FIDO2_ERR_UP_REQUIRED](#ga6b3b79c7ef54b3ebbe686d4f67aaf7fcaa28ed4a202b7c8eca14a727b708b0d50)、[FIDO2_ERR_UV_BLOCKED](#ga6b3b79c7ef54b3ebbe686d4f67aaf7fcaeb3d5db8b9e7ad3123df8d2a76ed4bfe)、[FIDO2_ERR_INTEGRITY_FAILURE](#ga6b3b79c7ef54b3ebbe686d4f67aaf7fca43b6e71c8f000bb2eccfc8a45c4591d3)、[FIDO2_ERR_INVALID_SUBCOMMAND](#ga6b3b79c7ef54b3ebbe686d4f67aaf7fca53aa4e296d54d24d7aab0bfc7747d893)、[FIDO2_ERR_UV_INVALID](#ga6b3b79c7ef54b3ebbe686d4f67aaf7fca620c7a76e1481401e9dce1a5a75c8ee8)、[FIDO2_ERR_UNAUTHORIZED_PERMISSION](#ga6b3b79c7ef54b3ebbe686d4f67aaf7fca69c9ebc7f40bcc26641eaa910a84f7e4)、[FIDO2_ERR_OTHER](#ga6b3b79c7ef54b3ebbe686d4f67aaf7fcab52bc5933983ff9464292f4a470e0217)。

CTAP2 状态码（Status Codes）。

<a id="r_gaec9e2106f2d776266909f5e2baf924d9"></a>

```c
enum fido2_cmd { FIDO2_CMD_MAKE_CREDENTIAL = 0x01 , FIDO2_CMD_GET_ASSERTION = 0x02 , FIDO2_CMD_GET_INFO = 0x04 , FIDO2_CMD_CLIENT_PIN = 0x06 , FIDO2_CMD_RESET = 0x07 , FIDO2_CMD_GET_NEXT_ASSERTION = 0x08 , FIDO2_CMD_CREDENTIAL_MGMT = 0x0A , FIDO2_CMD_SELECTION = 0x0B }
```

相关声明：[fido2_cmd](#gaec9e2106f2d776266909f5e2baf924d9)、[FIDO2_CMD_MAKE_CREDENTIAL](#gaec9e2106f2d776266909f5e2baf924d9aca44c6fcf4ff9f7d43693607a4ea178a)、[FIDO2_CMD_GET_ASSERTION](#gaec9e2106f2d776266909f5e2baf924d9a64758dfc5b08bccc58369e97ecd8eae0)、[FIDO2_CMD_GET_INFO](#gaec9e2106f2d776266909f5e2baf924d9a2419f886d7fcfe8e4e77a4b5f21d5bfc)、[FIDO2_CMD_CLIENT_PIN](#gaec9e2106f2d776266909f5e2baf924d9a6b7d85b947ad93ab5159ffe7f2934948)、[FIDO2_CMD_RESET](#gaec9e2106f2d776266909f5e2baf924d9aacffe603fa91c1102164c1d022bcd678)、[FIDO2_CMD_GET_NEXT_ASSERTION](#gaec9e2106f2d776266909f5e2baf924d9adc26ad4d923d58ca0f33d63c9dae1c27)、[FIDO2_CMD_CREDENTIAL_MGMT](#gaec9e2106f2d776266909f5e2baf924d9a4984d83c6210b1855106ff39b413e614)、[FIDO2_CMD_SELECTION](#gaec9e2106f2d776266909f5e2baf924d9a327a6fbfb22651dfed6d1d1ded574ab7)。

CTAP2 命令码（Command Codes）。

<a id="r_gae9411b5f6c2596cf49f7ebcf04fd7955"></a>

```c
enum fido2_cred_protect { FIDO2_CRED_PROTECT_UV_OPTIONAL = 0x01 , FIDO2_CRED_PROTECT_UV_OPTIONAL_WITH_LIST = 0x02 , FIDO2_CRED_PROTECT_UV_REQUIRED = 0x03 }
```

相关声明：[fido2_cred_protect](#gae9411b5f6c2596cf49f7ebcf04fd7955)、[FIDO2_CRED_PROTECT_UV_OPTIONAL](#gae9411b5f6c2596cf49f7ebcf04fd7955a07603aa0b0598319d504ca9e23e76078)、[FIDO2_CRED_PROTECT_UV_OPTIONAL_WITH_LIST](#gae9411b5f6c2596cf49f7ebcf04fd7955a2299549abdae08cd0e71c7db3d918ca6)、[FIDO2_CRED_PROTECT_UV_REQUIRED](#gae9411b5f6c2596cf49f7ebcf04fd7955aef0d3d870129fc9e72138d309c641be6)。

凭据保护级别（Credential Protection Levels）。

<a id="r_ga86aa0e78a95ea9e399c3831348fe8684"></a>

```c
enum fido2_cose_alg { FIDO2_COSE_ES256 = -7 , FIDO2_COSE_EDDSA = -8 , FIDO2_COSE_ECDHES_HKDF256 = -25 , FIDO2_COSE_RS256 = -257 }
```

相关声明：[fido2_cose_alg](#ga86aa0e78a95ea9e399c3831348fe8684)、[FIDO2_COSE_ES256](#ga86aa0e78a95ea9e399c3831348fe8684a94ae94ce511d5898c12059766adf95c3)、[FIDO2_COSE_EDDSA](#ga86aa0e78a95ea9e399c3831348fe8684a21d965a84070571fb2e0d475cf27043d)、[FIDO2_COSE_ECDHES_HKDF256](#ga86aa0e78a95ea9e399c3831348fe8684a386cd8a5baf42b49b2271d655645b103)、[FIDO2_COSE_RS256](#ga86aa0e78a95ea9e399c3831348fe8684ad2a327ca6649f0abd4153dee72952167)。

COSE 算法标识符（Algorithm Identifiers）。

<a id="r_ga7ff8f1d8d389b44e2a656b3ebe20f778"></a>

```c
#define FIDO2_CREDENTIAL_ID_MAX_SIZE 128
```

相关声明：[FIDO2_CREDENTIAL_ID_MAX_SIZE](#ga7ff8f1d8d389b44e2a656b3ebe20f778)。

FIDO2 共享类型（Shared Types）。

<a id="r_ga57628d326e2f62b318908af69485dbb8"></a>

```c
#define FIDO2_RP_ID_MAX_LEN 128
```

相关声明：[FIDO2_RP_ID_MAX_LEN](#ga57628d326e2f62b318908af69485dbb8)。

依赖方标识符（Relying Party ID）的最大长度。

<a id="r_ga99da0bebb5865edd2e163a31da966618"></a>

```c
#define FIDO2_RP_NAME_MAX_LEN 64
```

相关声明：[FIDO2_RP_NAME_MAX_LEN](#ga99da0bebb5865edd2e163a31da966618)。

依赖方名称（Relying Party Name）的最大长度。

<a id="r_ga6060501b6c00b076fc705276464050ab"></a>

```c
#define FIDO2_USER_NAME_MAX_LEN 64
```

相关声明：[FIDO2_USER_NAME_MAX_LEN](#ga6060501b6c00b076fc705276464050ab)。

用户名（User Name）的最大长度。

<a id="r_gaa4111c61a7446d3cb5efa41bf492d930"></a>

```c
#define FIDO2_USER_DISPLAY_NAME_MAX_LEN 64
```

相关声明：[FIDO2_USER_DISPLAY_NAME_MAX_LEN](#gaa4111c61a7446d3cb5efa41bf492d930)。

用户显示名称（User Display Name）的最大长度。

<a id="r_gaf5eb8fcafd96dd1d3eec5424aff9748c"></a>

```c
#define FIDO2_USER_ID_MAX_SIZE 64
```

相关声明：[FIDO2_USER_ID_MAX_SIZE](#gaf5eb8fcafd96dd1d3eec5424aff9748c)。

用户标识符（User ID）的最大大小，单位为字节。

<a id="r_ga624b79a13eb53f43594b5c24332725fa"></a>

```c
#define FIDO2_AAGUID_SIZE 16
```

相关声明：[FIDO2_AAGUID_SIZE](#ga624b79a13eb53f43594b5c24332725fa)。

认证器证明全局唯一标识符（AAGUID）的大小，单位为字节。

<a id="r_gaead02ba380ab3899742dfbf41edc4a98"></a>

```c
#define FIDO2_SHA256_SIZE 32
```

相关声明：[FIDO2_SHA256_SIZE](#gaead02ba380ab3899742dfbf41edc4a98)。

SHA-256 哈希大小（Hash Size）。

<a id="r_gaa42cec8a02f80b77e8ddf3250d4b289b"></a>

```c
#define FIDO2_PIN_HASH_SIZE 16
```

相关声明：[FIDO2_PIN_HASH_SIZE](#gaa42cec8a02f80b77e8ddf3250d4b289b)。

PIN 哈希大小（PIN Hash Size）。

<a id="r_ga0f2e24c8976c81ecceba0f65bf4ebdd6"></a>

```c
#define FIDO2_PIN_HASH_ENC_MAX_SIZE 32
```

相关声明：[FIDO2_PIN_HASH_ENC_MAX_SIZE](#ga0f2e24c8976c81ecceba0f65bf4ebdd6)。

加密 PIN 哈希（Encrypted PIN Hash）的最大大小。

<a id="r_gaefdcb90bad8ec73fe1fec85dd4bf3765"></a>

```c
#define FIDO2_PIN_ENC_MAX_SIZE 80
```

相关声明：[FIDO2_PIN_ENC_MAX_SIZE](#gaefdcb90bad8ec73fe1fec85dd4bf3765)。

加密 PIN（Encrypted PIN）的最大大小。

<a id="r_gad0a93bad80a62f314df813f979bbef25"></a>

```c
#define FIDO2_PIN_AUTH_SIZE_P1 16
```

相关声明：[FIDO2_PIN_AUTH_SIZE_P1](#gad0a93bad80a62f314df813f979bbef25)。

PIN 协议 1 认证参数大小（Auth Param Size）。

<a id="r_ga584ae6f184b200060162404c17f0391d"></a>

```c
#define FIDO2_PIN_AUTH_SIZE_P2 32
```

相关声明：[FIDO2_PIN_AUTH_SIZE_P2](#ga584ae6f184b200060162404c17f0391d)。

PIN 协议 2 认证参数大小（Auth Param Size）。

<a id="r_ga6deaa8990424ff5a31787753e60355d2"></a>

```c
#define FIDO2_PIN_AUTH_MAX_SIZE 32
```

相关声明：[FIDO2_PIN_AUTH_MAX_SIZE](#ga6deaa8990424ff5a31787753e60355d2)。

PIN 认证参数（Auth Param）的最大大小。

<a id="r_ga38ab5892a6d65b2ca4dab8cd59ea4567"></a>

```c
#define FIDO2_PIN_PADDED_SIZE 64
```

相关声明：[FIDO2_PIN_PADDED_SIZE](#ga38ab5892a6d65b2ca4dab8cd59ea4567)。

填充后的 PIN 大小（Padded PIN Size）。

<a id="r_gabeb1d03fa6426f2b7a8bf823a0cfd620"></a>

```c
#define FIDO2_PIN_TOKEN_ENC_MAX_SIZE 48
```

相关声明：[FIDO2_PIN_TOKEN_ENC_MAX_SIZE](#gabeb1d03fa6426f2b7a8bf823a0cfd620)。

加密 PIN 令牌大小（Encrypted PIN Token Size）。

<a id="r_ga8e68d9a5a88e01a964538d4cf457af85"></a>

```c
#define FIDO2_DISCOVERABLE_CRED_ID_SIZE 32
```

相关声明：[FIDO2_DISCOVERABLE_CRED_ID_SIZE](#ga8e68d9a5a88e01a964538d4cf457af85)。

可发现凭据标识符（Discoverable Credential ID）的大小。

<a id="r_gad0a496f504dea20073ae15be879086f6"></a>

```c
#define FIDO2_NON_DISCOVERABLE_CRED_ID_SIZE 64
```

相关声明：[FIDO2_NON_DISCOVERABLE_CRED_ID_SIZE](#gad0a496f504dea20073ae15be879086f6)。

不可发现凭据标识符（Non-discoverable Credential ID）的大小。

<a id="r_ga0288255da8902f9b30a345814419d06f"></a>

```c
#define FIDO2_AUTH_DATA_HEADER_SIZE 37
```

相关声明：[FIDO2_AUTH_DATA_HEADER_SIZE](#ga0288255da8902f9b30a345814419d06f)。

认证器数据头大小（Authenticator Data Header Size）。

<a id="r_gafb170c684357560e3c5999b3ae7aef80"></a>

```c
#define FIDO2_ATTESTED_CRED_DATA_MAX_SIZE (FIDO2_AAGUID_SIZE + 2 + FIDO2_CREDENTIAL_ID_MAX_SIZE + FIDO2_COSE_KEY_MAX_SIZE)
```

相关声明：[FIDO2_ATTESTED_CRED_DATA_MAX_SIZE](#gafb170c684357560e3c5999b3ae7aef80)、[FIDO2_AAGUID_SIZE](#ga624b79a13eb53f43594b5c24332725fa)、[FIDO2_CREDENTIAL_ID_MAX_SIZE](#ga7ff8f1d8d389b44e2a656b3ebe20f778)。

证明凭据数据大小（Attested Credential Data Size）。

<a id="r_ga20de82a88a0f0d1c5e2f590450da98b3"></a>

```c
#define FIDO2_AUTH_DATA_MAX_SIZE (FIDO2_AUTH_DATA_HEADER_SIZE + FIDO2_ATTESTED_CRED_DATA_MAX_SIZE)
```

相关声明：[FIDO2_AUTH_DATA_MAX_SIZE](#ga20de82a88a0f0d1c5e2f590450da98b3)、[FIDO2_AUTH_DATA_HEADER_SIZE](#ga0288255da8902f9b30a345814419d06f)、[FIDO2_ATTESTED_CRED_DATA_MAX_SIZE](#gafb170c684357560e3c5999b3ae7aef80)。

authenticatorData 最大大小（Maximum Size）8。

<a id="r_ga7fe764c73ecb327210eb080aa5b32a92"></a>

```c
#define FIDO2_MAX_EXTENSIONS 8
```

相关声明：[FIDO2_MAX_EXTENSIONS](#ga7fe764c73ecb327210eb080aa5b32a92)。

支持的扩展（Extensions）的最大数量。

<a id="r_ga15f94b65bca9940f1a535e6ec1339fdf"></a>

```c
#define FIDO2_MAX_VERSIONS 4
```

相关声明：[FIDO2_MAX_VERSIONS](#ga15f94b65bca9940f1a535e6ec1339fdf)。

支持的版本（Versions）的最大数量。

<a id="r_ga21282c628cd729631d3e02464693d454"></a>

```c
#define FIDO2_P256_UNCOMPRESSED_KEY_SIZE 65
```

相关声明：[FIDO2_P256_UNCOMPRESSED_KEY_SIZE](#ga21282c628cd729631d3e02464693d454)。

P-256 公钥导出大小（Public Key Export Size）。

<a id="r_ga03768c49b649e417454b17351825c89f"></a>

```c
#define FIDO2_P256_COORD_SIZE 32
```

相关声明：[FIDO2_P256_COORD_SIZE](#ga03768c49b649e417454b17351825c89f)。

P-256 坐标大小（Coordinate Size）。

<a id="r_gaa54dab9d9f69e30167e8e26b57750d03"></a>

```c
#define FIDO2_EC_POINT_UNCOMPRESSED 0x04
```

相关声明：[FIDO2_EC_POINT_UNCOMPRESSED](#gaa54dab9d9f69e30167e8e26b57750d03)。

椭圆曲线点前缀（EC Point Prefix）。

<a id="r_gadd8a4b5d7acd36c8eef7e593ece7f9ba"></a>

```c
#define FIDO2_ECDSA_SIG_MAX_SIZE 72
```

相关声明：[FIDO2_ECDSA_SIG_MAX_SIZE](#gadd8a4b5d7acd36c8eef7e593ece7f9ba)。

ASN.1 编码的 ECDSA 签名长度（Signature Length）。

<a id="r_gae9b40fa6a6e68946588075afc6fe770a"></a>

```c
#define FIDO2_EXT_HMAC_SECRET BIT(0)
```

相关声明：[FIDO2_EXT_HMAC_SECRET](#gae9b40fa6a6e68946588075afc6fe770a)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

凭据扩展（Credential Extension）：HMAC secret。

<a id="r_ga8ec5a639800de3f326a963188f1d9426"></a>

```c
#define FIDO2_EXT_LARGE_BLOB_KEY BIT(1)
```

相关声明：[FIDO2_EXT_LARGE_BLOB_KEY](#ga8ec5a639800de3f326a963188f1d9426)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

凭据扩展（Credential Extension）：largeBlobKey。

<a id="r_ga6ce7d790ac95281ddf48fdfcc26e62b1"></a>

```c
#define FIDO2_EXT_CRED_BLOB BIT(2)
```

相关声明：[FIDO2_EXT_CRED_BLOB](#ga6ce7d790ac95281ddf48fdfcc26e62b1)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

凭据扩展（Credential Extension）：credBlob。

<a id="r_ga014d98ca20bdba2ec3e03de0ce074221"></a>

```c
#define FIDO2_EXT_THIRD_PARTY_PAY BIT(3)
```

相关声明：[FIDO2_EXT_THIRD_PARTY_PAY](#ga014d98ca20bdba2ec3e03de0ce074221)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

凭据扩展（Credential Extension）：thirdPartyPayment。

<a id="r_ga3e2b16dffcd2c4a5b8958c5473a49bce"></a>

```c
#define FIDO2_TRANSPORT_USB BIT(0)
```

相关声明：[FIDO2_TRANSPORT_USB](#ga3e2b16dffcd2c4a5b8958c5473a49bce)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

USB 传输（Transport）。

<a id="r_ga70811c17432b511a72481030abe09b2e"></a>

```c
#define FIDO2_TRANSPORT_BLE BIT(1)
```

相关声明：[FIDO2_TRANSPORT_BLE](#ga70811c17432b511a72481030abe09b2e)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

低功耗蓝牙（BLE）传输（Transport）。

<a id="r_ga6b1cc385bcce20455922f617c8221f98"></a>

```c
#define FIDO2_TRANSPORT_NFC BIT(2)
```

相关声明：[FIDO2_TRANSPORT_NFC](#ga6b1cc385bcce20455922f617c8221f98)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

近场通信（NFC）传输（Transport）。

<a id="r_ga82f1ff43692a451fcd11ec623165db6e"></a>

```c
#define AUTH_DATA_FLAG_UP BIT(0)
```

相关声明：[AUTH_DATA_FLAG_UP](#ga82f1ff43692a451fcd11ec623165db6e)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

用户在场（User Present，UP）结果。

<a id="r_gac08abdf137cc2062f0e4b4a81ee2802b"></a>

```c
#define AUTH_DATA_FLAG_UV BIT(2)
```

相关声明：[AUTH_DATA_FLAG_UV](#gac08abdf137cc2062f0e4b4a81ee2802b)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

用户已验证（User Verified，UV）结果。

<a id="r_ga66a31ee72d63974ac4838f35149cd1d9"></a>

```c
#define AUTH_DATA_FLAG_AT BIT(6)
```

相关声明：[AUTH_DATA_FLAG_AT](#ga66a31ee72d63974ac4838f35149cd1d9)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

包含证明凭据数据（Attested Credential Data，AT）。

<a id="r_ga01d9f3d9e550f3cf16083d8048b6c6b4"></a>

```c
#define AUTH_DATA_FLAG_ED BIT(7)
```

相关声明：[AUTH_DATA_FLAG_ED](#ga01d9f3d9e550f3cf16083d8048b6c6b4)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

包含扩展数据（Extension Data，ED）。

<a id="r_gad0f22c2a4c49fdd7b47ed0913115c5b2"></a>

```c
typedef int(* fido2_storage_iterate_cb_t) (const struct fido2_credential *cred, void *user_data)
```

相关声明：[fido2_storage_iterate_cb_t](#gad0f22c2a4c49fdd7b47ed0913115c5b2)、[fido2_credential](../platform_security_model_reference/P007_fido2_credential_结构体.md)。

FIDO2 凭据存储（Credential Storage）。

<a id="r_ga27aa8972d17b4ee6454204d0ab527ed0"></a>

```c
const struct fido2_storage_api fido2_storage_backend
```

相关声明：[fido2_storage_api](../platform_security_model_reference/P009_fido2_storage_api_结构体.md)、[fido2_storage_backend](#ga27aa8972d17b4ee6454204d0ab527ed0)。

FIDO2 存储后端实例（Storage Backend Instance）。

<a id="r_gab782d78847a38dd7aeac52a806879dfb"></a>

```c
int fido2_up_wait (void)
```

相关声明：[fido2_up_wait](#gab782d78847a38dd7aeac52a806879dfb)。

FIDO2 用户在场（User Presence）。

<a id="r_gae7fb0da6d327ef0be220d32558ea6be2"></a>

```c
void fido2_up_reset (void)
```

相关声明：[fido2_up_reset](#gae7fb0da6d327ef0be220d32558ea6be2)。

为新请求（Request）重置用户在场状态（User-Presence State）。

<a id="r_gaf6d50aa0022f56350a927149086d7838"></a>

```c
void fido2_up_cancel (void)
```

相关声明：[fido2_up_cancel](#gaf6d50aa0022f56350a927149086d7838)。

取消尚未完成的用户在场等待（Pending User Presence Wait）。

<a id="r_gaf81f2aff090633c893740db7b60ed614"></a>

```c
int fido2_attestation_sign (const uint8_t *auth_data, size_t auth_data_len, const uint8_t *client_data_hash, uint32_t credential_key_id, struct fido2_attestation_result *result)
```

相关声明：[fido2_attestation_sign](#gaf81f2aff090633c893740db7b60ed614)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[fido2_attestation_result](../platform_security_model_reference/P006_fido2_attestation_result_结构体.md)。

为新凭据（Credential）签署 `authenticatorData`。

<a id="r_gaa8a025dbfc332bb3b8b3829b3f4bda69"></a>

```c
#define FIDO2_ATTESTATION_FMT_PACKED "packed"
```

相关声明：[FIDO2_ATTESTATION_FMT_PACKED](#gaa8a025dbfc332bb3b8b3829b3f4bda69)。

FIDO2 证明（Attestation）。

<a id="r_ga09c488599bae6b3454023bf696ecd6e0"></a>

```c
#define FIDO2_ATTESTATION_FMT_NONE "none"
```

相关声明：[FIDO2_ATTESTATION_FMT_NONE](#ga09c488599bae6b3454023bf696ecd6e0)。

不提供证明（No Attestation）。

<a id="r_ga25c2604da4e7adb9ec186a846265b1bc"></a>

```c
#define FIDO2_ATTESTATION_FMT_MAX_LEN 32
```

相关声明：[FIDO2_ATTESTATION_FMT_MAX_LEN](#ga25c2604da4e7adb9ec186a846265b1bc)。

证明格式标识（Attestation Format Identifier）的最大长度。

## 8.5\_详细说明（Detailed Documentation）

<a id="ga66a31ee72d63974ac4838f35149cd1d9"></a>

### `AUTH_DATA_FLAG_AT`

```c
#define AUTH_DATA_FLAG_AT BIT(6)
```

```c
#include <zephyr/authentication/fido2/fido2_types.h>
```

包含证明凭据数据（Attested Credential Data，AT）。

<a id="ga01d9f3d9e550f3cf16083d8048b6c6b4"></a>

### `AUTH_DATA_FLAG_ED`

```c
#define AUTH_DATA_FLAG_ED BIT(7)
```

```c
#include <zephyr/authentication/fido2/fido2_types.h>
```

包含扩展数据（Extension Data，ED）。

<a id="ga82f1ff43692a451fcd11ec623165db6e"></a>

### `AUTH_DATA_FLAG_UP`

```c
#define AUTH_DATA_FLAG_UP BIT(0)
```

```c
#include <zephyr/authentication/fido2/fido2_types.h>
```

用户在场（User Present，UP）结果。

<a id="gac08abdf137cc2062f0e4b4a81ee2802b"></a>

### `AUTH_DATA_FLAG_UV`

```c
#define AUTH_DATA_FLAG_UV BIT(2)
```

```c
#include <zephyr/authentication/fido2/fido2_types.h>
```

用户已验证（User Verified，UV）结果。

<a id="ga624b79a13eb53f43594b5c24332725fa"></a>

### `FIDO2_AAGUID_SIZE`

```c
#define FIDO2_AAGUID_SIZE 16
```

```c
#include <zephyr/authentication/fido2/fido2_types.h>
```

认证器证明全局唯一标识符（AAGUID）的大小，单位为字节。

<a id="ga25c2604da4e7adb9ec186a846265b1bc"></a>

### `FIDO2_ATTESTATION_FMT_MAX_LEN`

```c
#define FIDO2_ATTESTATION_FMT_MAX_LEN 32
```

```c
#include <zephyr/authentication/fido2/fido2_attestation.h>
```

证明格式标识（Attestation Format Identifier）的最大长度。

<a id="ga09c488599bae6b3454023bf696ecd6e0"></a>

### `FIDO2_ATTESTATION_FMT_NONE`

```c
#define FIDO2_ATTESTATION_FMT_NONE "none"
```

```c
#include <zephyr/authentication/fido2/fido2_attestation.h>
```

不提供证明（No Attestation）。

<a id="gaa8a025dbfc332bb3b8b3829b3f4bda69"></a>

### `FIDO2_ATTESTATION_FMT_PACKED`

```c
#define FIDO2_ATTESTATION_FMT_PACKED "packed"
```

```c
#include <zephyr/authentication/fido2/fido2_attestation.h>
```

FIDO2 证明（Attestation）。

打包证明（Packed Attestation）。

<a id="gafb170c684357560e3c5999b3ae7aef80"></a>

### `FIDO2_ATTESTED_CRED_DATA_MAX_SIZE`

```c
#define FIDO2_ATTESTED_CRED_DATA_MAX_SIZE (FIDO2_AAGUID_SIZE + 2 + FIDO2_CREDENTIAL_ID_MAX_SIZE + FIDO2_COSE_KEY_MAX_SIZE)
```

```c
#include <zephyr/authentication/fido2/fido2_types.h>
```

证明凭据数据大小（Attested Credential Data Size）。

<a id="ga0288255da8902f9b30a345814419d06f"></a>

### `FIDO2_AUTH_DATA_HEADER_SIZE`

```c
#define FIDO2_AUTH_DATA_HEADER_SIZE 37
```

```c
#include <zephyr/authentication/fido2/fido2_types.h>
```

认证器数据头大小（Authenticator Data Header Size）。

<a id="ga20de82a88a0f0d1c5e2f590450da98b3"></a>

### `FIDO2_AUTH_DATA_MAX_SIZE`

```c
#define FIDO2_AUTH_DATA_MAX_SIZE (FIDO2_AUTH_DATA_HEADER_SIZE + FIDO2_ATTESTED_CRED_DATA_MAX_SIZE)
```

```c
#include <zephyr/authentication/fido2/fido2_types.h>
```

authenticatorData 最大大小（Maximum Size）8。

<a id="ga7ff8f1d8d389b44e2a656b3ebe20f778"></a>

### `FIDO2_CREDENTIAL_ID_MAX_SIZE`

```c
#define FIDO2_CREDENTIAL_ID_MAX_SIZE 128
```

```c
#include <zephyr/authentication/fido2/fido2_types.h>
```

FIDO2 共享类型（Shared Types）。

凭据标识符（Credential ID）的最大大小，以字节为单位。

<a id="ga8e68d9a5a88e01a964538d4cf457af85"></a>

### `FIDO2_DISCOVERABLE_CRED_ID_SIZE`

```c
#define FIDO2_DISCOVERABLE_CRED_ID_SIZE 32
```

```c
#include <zephyr/authentication/fido2/fido2_types.h>
```

可发现凭据标识符（Discoverable Credential ID）的大小。

<a id="gaa54dab9d9f69e30167e8e26b57750d03"></a>

### `FIDO2_EC_POINT_UNCOMPRESSED`

```c
#define FIDO2_EC_POINT_UNCOMPRESSED 0x04
```

```c
#include <zephyr/authentication/fido2/fido2_types.h>
```

椭圆曲线点前缀（EC Point Prefix）。

<a id="gadd8a4b5d7acd36c8eef7e593ece7f9ba"></a>

### `FIDO2_ECDSA_SIG_MAX_SIZE`

```c
#define FIDO2_ECDSA_SIG_MAX_SIZE 72
```

```c
#include <zephyr/authentication/fido2/fido2_types.h>
```

ASN.1 编码的 ECDSA 签名长度（Signature Length）。

<a id="ga6ce7d790ac95281ddf48fdfcc26e62b1"></a>

### `FIDO2_EXT_CRED_BLOB`

```c
#define FIDO2_EXT_CRED_BLOB BIT(2)
```

```c
#include <zephyr/authentication/fido2/fido2_types.h>
```

凭据扩展（Credential Extension）：credBlob。

<a id="gae9b40fa6a6e68946588075afc6fe770a"></a>

### `FIDO2_EXT_HMAC_SECRET`

```c
#define FIDO2_EXT_HMAC_SECRET BIT(0)
```

```c
#include <zephyr/authentication/fido2/fido2_types.h>
```

凭据扩展（Credential Extension）：HMAC secret。

<a id="ga8ec5a639800de3f326a963188f1d9426"></a>

### `FIDO2_EXT_LARGE_BLOB_KEY`

```c
#define FIDO2_EXT_LARGE_BLOB_KEY BIT(1)
```

```c
#include <zephyr/authentication/fido2/fido2_types.h>
```

凭据扩展（Credential Extension）：largeBlobKey。

<a id="ga014d98ca20bdba2ec3e03de0ce074221"></a>

### `FIDO2_EXT_THIRD_PARTY_PAY`

```c
#define FIDO2_EXT_THIRD_PARTY_PAY BIT(3)
```

```c
#include <zephyr/authentication/fido2/fido2_types.h>
```

凭据扩展（Credential Extension）：thirdPartyPayment。

<a id="ga7fe764c73ecb327210eb080aa5b32a92"></a>

### `FIDO2_MAX_EXTENSIONS`

```c
#define FIDO2_MAX_EXTENSIONS 8
```

```c
#include <zephyr/authentication/fido2/fido2_types.h>
```

支持的扩展（Extensions）的最大数量。

<a id="ga15f94b65bca9940f1a535e6ec1339fdf"></a>

### `FIDO2_MAX_VERSIONS`

```c
#define FIDO2_MAX_VERSIONS 4
```

```c
#include <zephyr/authentication/fido2/fido2_types.h>
```

支持的版本（Versions）的最大数量。

<a id="gad0a496f504dea20073ae15be879086f6"></a>

### `FIDO2_NON_DISCOVERABLE_CRED_ID_SIZE`

```c
#define FIDO2_NON_DISCOVERABLE_CRED_ID_SIZE 64
```

```c
#include <zephyr/authentication/fido2/fido2_types.h>
```

不可发现凭据标识符（Non-discoverable Credential ID）的大小。

<a id="ga03768c49b649e417454b17351825c89f"></a>

### `FIDO2_P256_COORD_SIZE`

```c
#define FIDO2_P256_COORD_SIZE 32
```

```c
#include <zephyr/authentication/fido2/fido2_types.h>
```

P-256 坐标大小（Coordinate Size）。

<a id="ga21282c628cd729631d3e02464693d454"></a>

### `FIDO2_P256_UNCOMPRESSED_KEY_SIZE`

```c
#define FIDO2_P256_UNCOMPRESSED_KEY_SIZE 65
```

```c
#include <zephyr/authentication/fido2/fido2_types.h>
```

P-256 公钥导出大小（Public Key Export Size）。

<a id="ga6deaa8990424ff5a31787753e60355d2"></a>

### `FIDO2_PIN_AUTH_MAX_SIZE`

```c
#define FIDO2_PIN_AUTH_MAX_SIZE 32
```

```c
#include <zephyr/authentication/fido2/fido2_types.h>
```

PIN 认证参数（Auth Param）的最大大小。

<a id="gad0a93bad80a62f314df813f979bbef25"></a>

### `FIDO2_PIN_AUTH_SIZE_P1`

```c
#define FIDO2_PIN_AUTH_SIZE_P1 16
```

```c
#include <zephyr/authentication/fido2/fido2_types.h>
```

PIN 协议 1 认证参数大小（Auth Param Size）。

<a id="ga584ae6f184b200060162404c17f0391d"></a>

### `FIDO2_PIN_AUTH_SIZE_P2`

```c
#define FIDO2_PIN_AUTH_SIZE_P2 32
```

```c
#include <zephyr/authentication/fido2/fido2_types.h>
```

PIN 协议 2 认证参数大小（Auth Param Size）。

<a id="gaefdcb90bad8ec73fe1fec85dd4bf3765"></a>

### `FIDO2_PIN_ENC_MAX_SIZE`

```c
#define FIDO2_PIN_ENC_MAX_SIZE 80
```

```c
#include <zephyr/authentication/fido2/fido2_types.h>
```

加密 PIN（Encrypted PIN）的最大大小。

<a id="ga0f2e24c8976c81ecceba0f65bf4ebdd6"></a>

### `FIDO2_PIN_HASH_ENC_MAX_SIZE`

```c
#define FIDO2_PIN_HASH_ENC_MAX_SIZE 32
```

```c
#include <zephyr/authentication/fido2/fido2_types.h>
```

加密 PIN 哈希（Encrypted PIN Hash）的最大大小。

<a id="gaa42cec8a02f80b77e8ddf3250d4b289b"></a>

### `FIDO2_PIN_HASH_SIZE`

```c
#define FIDO2_PIN_HASH_SIZE 16
```

```c
#include <zephyr/authentication/fido2/fido2_types.h>
```

PIN 哈希大小（PIN Hash Size）。

<a id="ga38ab5892a6d65b2ca4dab8cd59ea4567"></a>

### `FIDO2_PIN_PADDED_SIZE`

```c
#define FIDO2_PIN_PADDED_SIZE 64
```

```c
#include <zephyr/authentication/fido2/fido2_types.h>
```

填充后的 PIN 大小（Padded PIN Size）。

<a id="gabeb1d03fa6426f2b7a8bf823a0cfd620"></a>

### `FIDO2_PIN_TOKEN_ENC_MAX_SIZE`

```c
#define FIDO2_PIN_TOKEN_ENC_MAX_SIZE 48
```

```c
#include <zephyr/authentication/fido2/fido2_types.h>
```

加密 PIN 令牌大小（Encrypted PIN Token Size）。

<a id="ga57628d326e2f62b318908af69485dbb8"></a>

### `FIDO2_RP_ID_MAX_LEN`

```c
#define FIDO2_RP_ID_MAX_LEN 128
```

```c
#include <zephyr/authentication/fido2/fido2_types.h>
```

依赖方标识符（Relying Party ID）的最大长度。

<a id="ga99da0bebb5865edd2e163a31da966618"></a>

### `FIDO2_RP_NAME_MAX_LEN`

```c
#define FIDO2_RP_NAME_MAX_LEN 64
```

```c
#include <zephyr/authentication/fido2/fido2_types.h>
```

依赖方名称（Relying Party Name）的最大长度。

<a id="gaead02ba380ab3899742dfbf41edc4a98"></a>

### `FIDO2_SHA256_SIZE`

```c
#define FIDO2_SHA256_SIZE 32
```

```c
#include <zephyr/authentication/fido2/fido2_types.h>
```

SHA-256 哈希大小（Hash Size）。

<a id="ga70811c17432b511a72481030abe09b2e"></a>

### `FIDO2_TRANSPORT_BLE`

```c
#define FIDO2_TRANSPORT_BLE BIT(1)
```

```c
#include <zephyr/authentication/fido2/fido2_types.h>
```

低功耗蓝牙（BLE）传输（Transport）。

<a id="ga6b1cc385bcce20455922f617c8221f98"></a>

### `FIDO2_TRANSPORT_NFC`

```c
#define FIDO2_TRANSPORT_NFC BIT(2)
```

```c
#include <zephyr/authentication/fido2/fido2_types.h>
```

近场通信（NFC）传输（Transport）。

<a id="ga3e2b16dffcd2c4a5b8958c5473a49bce"></a>

### `FIDO2_TRANSPORT_USB`

```c
#define FIDO2_TRANSPORT_USB BIT(0)
```

```c
#include <zephyr/authentication/fido2/fido2_types.h>
```

USB 传输（Transport）。

<a id="gaa4111c61a7446d3cb5efa41bf492d930"></a>

### `FIDO2_USER_DISPLAY_NAME_MAX_LEN`

```c
#define FIDO2_USER_DISPLAY_NAME_MAX_LEN 64
```

```c
#include <zephyr/authentication/fido2/fido2_types.h>
```

用户显示名称（User Display Name）的最大长度。

<a id="gaf5eb8fcafd96dd1d3eec5424aff9748c"></a>

### `FIDO2_USER_ID_MAX_SIZE`

```c
#define FIDO2_USER_ID_MAX_SIZE 64
```

```c
#include <zephyr/authentication/fido2/fido2_types.h>
```

用户标识符（User ID）的最大大小，单位为字节。

<a id="ga6060501b6c00b076fc705276464050ab"></a>

### `FIDO2_USER_NAME_MAX_LEN`

```c
#define FIDO2_USER_NAME_MAX_LEN 64
```

```c
#include <zephyr/authentication/fido2/fido2_types.h>
```

用户名（User Name）的最大长度。

<a id="gad0a191f4a48998fe857dc6315d225d94"></a>

### `fido2_state_callback_t`

```c
typedef void(* fido2_state_callback_t) (enum fido2_runtime_state state, void *user_data)
```

```c
#include <zephyr/authentication/fido2/fido2.h>
```

FIDO2 运行时状态回调（Runtime State Callback）。

FIDO2 运行时状态（Runtime State）变化时调用。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `state` | 新的运行时状态（Runtime State）。 |
| `user_data` | 设置回调时提供的不透明上下文指针（Opaque Context Pointer）。 |

**说明（Note）**：注意（Note）：此回调同步（Synchronously）调用。运行时状态转换（Runtime State Transition）从 FIDO2 内部线程／工作队列上下文（Thread/Workqueue Context）报告。回调必须轻量，不能长时间阻塞。

<a id="gad0f22c2a4c49fdd7b47ed0913115c5b2"></a>

### `fido2_storage_iterate_cb_t`

```c
typedef int(* fido2_storage_iterate_cb_t) (const struct fido2_credential *cred, void *user_data)
```

```c
#include <zephyr/authentication/fido2/fido2_storage.h>
```

FIDO2 凭据存储（Credential Storage）。

用于枚举凭据（Enumerating Credentials）的回调。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `cred` | 当前凭据（Current Credential）。 |
| `user_data` | 不透明用户上下文（Opaque User Context）。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 继续枚举（Enumeration）。 |
| `non-zero` | 停止枚举（Enumeration）；此值会传递给 `fido2_storage_iterate()`。 |

<a id="gaec9e2106f2d776266909f5e2baf924d9"></a>

### `fido2_cmd`

```c
enum fido2_cmd
```

```c
#include <zephyr/authentication/fido2/fido2_types.h>
```

CTAP2 命令码（Command Codes）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `FIDO2_CMD_MAKE_CREDENTIAL` | 创建新凭据（Credential）。 |
| `FIDO2_CMD_GET_ASSERTION` | 使用凭据（Credential）进行认证（Authentication）。 |
| `FIDO2_CMD_GET_INFO` | 获取认证器信息（Authenticator Info）。 |
| `FIDO2_CMD_CLIENT_PIN` | 客户端个人识别码操作（Client PIN Operations）。 |
| `FIDO2_CMD_RESET` | 恢复出厂设置（Factory Reset）。 |
| `FIDO2_CMD_GET_NEXT_ASSERTION` | 获取下一个断言（Assertion）。 |
| `FIDO2_CMD_CREDENTIAL_MGMT` | 凭据管理（Credential Management）。 |
| `FIDO2_CMD_SELECTION` | 认证器选择（Authenticator Selection）。 |

<a id="ga86aa0e78a95ea9e399c3831348fe8684"></a>

### `fido2_cose_alg`

```c
enum fido2_cose_alg
```

```c
#include <zephyr/authentication/fido2/fido2_types.h>
```

COSE 算法标识符（Algorithm Identifiers）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `FIDO2_COSE_ES256` | 使用 SHA-256 的椭圆曲线数字签名算法（ECDSA）。 |
| `FIDO2_COSE_EDDSA` | 爱德华曲线数字签名算法（EdDSA）。 |
| `FIDO2_COSE_ECDHES_HKDF256` | 使用 HKDF 的椭圆曲线 Diffie–Hellman 临时—静态密钥协商（ECDH ES）。 |
| `FIDO2_COSE_RS256` | 使用 SHA-256 的 RSASSA-PKCS1-v1_5 签名算法。 |

<a id="gae9411b5f6c2596cf49f7ebcf04fd7955"></a>

### `fido2_cred_protect`

```c
enum fido2_cred_protect
```

```c
#include <zephyr/authentication/fido2/fido2_types.h>
```

凭据保护级别（Credential Protection Levels）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `FIDO2_CRED_PROTECT_UV_OPTIONAL` | 用户验证（UV）可选；不执行验证也可使用凭据（Credential）。 |
| `FIDO2_CRED_PROTECT_UV_OPTIONAL_WITH_LIST` | 用户验证（UV）可选；只有提供凭据标识符列表（Credential ID List）时才能使用凭据。 |
| `FIDO2_CRED_PROTECT_UV_REQUIRED` | 用户验证（UV）必需；凭据（Credential）始终要求用户验证。 |

<a id="gabf5068079e94310fb4b942df56ec1d10"></a>

### `fido2_runtime_state`

```c
enum fido2_runtime_state
```

```c
#include <zephyr/authentication/fido2/fido2.h>
```

FIDO2 子系统对外提供的运行时状态（Runtime States）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `FIDO2_RUNTIME_STATE_STOPPED` | FIDO2 已停止，且不处理命令（Command）。 |
| `FIDO2_RUNTIME_STATE_IDLE` | FIDO2 正在运行，处于空闲状态（Idle）。 |
| `FIDO2_RUNTIME_STATE_WAITING_USER_PRESENCE` | FIDO2 正在等待用户在场确认（User Presence Confirmation）。 |
| `FIDO2_RUNTIME_STATE_PROCESSING` | FIDO2 正在用户在场（User Presence）确认后处理命令。 |

<a id="ga6b3b79c7ef54b3ebbe686d4f67aaf7fc"></a>

### `fido2_status`

```c
enum fido2_status
```

```c
#include <zephyr/authentication/fido2/fido2_types.h>
```

CTAP2 状态码（Status Codes）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `FIDO2_OK` | 成功。 |
| `FIDO2_ERR_INVALID_COMMAND` | 无效命令（Invalid Command）。 |
| `FIDO2_ERR_INVALID_PARAMETER` | 参数无效（Invalid Parameter）。 |
| `FIDO2_ERR_INVALID_LENGTH` | 消息长度（Message Length）无效。 |
| `FIDO2_ERR_INVALID_SEQ` | 序列号（Sequence Number）无效。 |
| `FIDO2_ERR_TIMEOUT` | 请求超时（Request Timed Out）。 |
| `FIDO2_ERR_CHANNEL_BUSY` | 通道忙（Channel Busy）。 |
| `FIDO2_ERR_LOCK_REQUIRED` | 命令需要锁（Lock）。 |
| `FIDO2_ERR_INVALID_CHANNEL` | 通道（Channel）无效。 |
| `FIDO2_ERR_CBOR_UNEXPECTED_TYPE` | 非预期的简明二进制对象表示（CBOR）类型。 |
| `FIDO2_ERR_INVALID_CBOR` | 简明二进制对象表示（CBOR）编码无效。 |
| `FIDO2_ERR_MISSING_PARAMETER` | 缺少必需参数（Required Parameter）。 |
| `FIDO2_ERR_LIMIT_EXCEEDED` | 超出限制（Limit Exceeded）。 |
| `FIDO2_ERR_UNSUPPORTED_EXTENSION` | 不支持的扩展（Extension）。 |
| `FIDO2_ERR_FP_DATABASE_FULL` | 指纹数据库（Fingerprint Database）已满。 |
| `FIDO2_ERR_LARGE_BLOB_STORAGE_FULL` | 大二进制对象存储（Large Blob Storage）已满。 |
| `FIDO2_ERR_CREDENTIAL_EXCLUDED` | 在 `excludeList` 中找到了凭据（Credential）。 |
| `FIDO2_ERR_PROCESSING` | 处理中（Processing）。 |
| `FIDO2_ERR_INVALID_CREDENTIAL` | 凭据（Credential）无效。 |
| `FIDO2_ERR_USER_ACTION_PENDING` | 等待用户操作（User Action）。 |
| `FIDO2_ERR_OPERATION_PENDING` | 操作待处理（Operation Pending）。 |
| `FIDO2_ERR_NO_OPERATIONS` | 没有待处理操作（Pending Operations）。 |
| `FIDO2_ERR_UNSUPPORTED_ALGORITHM` | 不支持的算法（Algorithm）。 |
| `FIDO2_ERR_OPERATION_DENIED` | 操作被拒绝（Operation Denied）。 |
| `FIDO2_ERR_KEY_STORE_FULL` | 密钥存储（Key Store）已满。 |
| `FIDO2_ERR_UNSUPPORTED_OPTION` | 不支持的选项（Option）。 |
| `FIDO2_ERR_INVALID_OPTION` | 选项值（Option Value）对当前操作无效。 |
| `FIDO2_ERR_KEEPALIVE_CANCEL` | 平台（Platform）已取消保活（Keepalive）。 |
| `FIDO2_ERR_NO_CREDENTIALS` | 未找到凭据（Credentials）。 |
| `FIDO2_ERR_USER_ACTION_TIMEOUT` | 用户操作超时（User Action Timed Out）。 |
| `FIDO2_ERR_NOT_ALLOWED` | 不允许执行该操作（Operation Not Allowed）。 |
| `FIDO2_ERR_PIN_INVALID` | 个人识别码（PIN）无效。 |
| `FIDO2_ERR_PIN_BLOCKED` | 个人识别码（PIN）已被锁定（Blocked）。 |
| `FIDO2_ERR_PIN_AUTH_INVALID` | PIN 认证校验（PIN Auth Verification）失败。 |
| `FIDO2_ERR_PIN_AUTH_BLOCKED` | PIN 认证（PIN Auth）已被锁定（Blocked）。 |
| `FIDO2_ERR_PIN_NOT_SET` | 尚未设置个人识别码（PIN）。 |
| `FIDO2_ERR_PUAT_REQUIRED` | 需要 PIN／用户验证认证令牌（PIN/UV Auth Token）。 |
| `FIDO2_ERR_PIN_POLICY_VIOLATION` | 违反 PIN 策略（PIN Policy Violation）。 |
| `FIDO2_ERR_RESERVED` | PIN／用户验证认证令牌（PIN/UV Auth Token）已过期。 |
| `FIDO2_ERR_REQUEST_TOO_LARGE` | 请求超过 `maxMsgSize`。 |
| `FIDO2_ERR_ACTION_TIMEOUT` | 平台响应超时（Platform Response Timed Out）。 |
| `FIDO2_ERR_UP_REQUIRED` | 需要用户在场（User Presence）。 |
| `FIDO2_ERR_UV_BLOCKED` | 用户验证（User Verification）已被锁定（Blocked）。 |
| `FIDO2_ERR_INTEGRITY_FAILURE` | 认证器完整性检查（Authenticator Integrity Check）失败。 |
| `FIDO2_ERR_INVALID_SUBCOMMAND` | 该命令的子命令（Subcommand）无效。 |
| `FIDO2_ERR_UV_INVALID` | 用户验证（User Verification）失败。 |
| `FIDO2_ERR_UNAUTHORIZED_PERMISSION` | PIN／用户验证令牌（PIN/UV Token）缺少权限（Permission）。 |
| `FIDO2_ERR_OTHER` | 其他未指定错误（Unspecified Error）。 |

<a id="gaf81f2aff090633c893740db7b60ed614"></a>

### `fido2_attestation_sign()`

```c
int fido2_attestation_sign ( const uint8_t * auth_data, size_t auth_data_len, const uint8_t * client_data_hash, uint32_t credential_key_id, struct fido2_attestation_result * result )
```

```c
#include <zephyr/authentication/fido2/fido2_attestation.h>
```

为新凭据（Credential）签署 `authenticatorData`。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `auth_data` | 原始 `authenticatorData` 字节（Raw Bytes）。 |
| `auth_data_len` | `auth_data` 的长度（Length）。 |
| `client_data_hash` | `clientDataJSON` 的 32 字节 SHA-256 摘要。 |
| `credential_key_id` | 凭据密钥（Credential Key）的 PSA 密钥句柄（Key Handle）。仅用于自证明（Self-attestation）。 |
| `result` | 待填充的证明结果（Attestation Result）。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功时返回。 |
| `-errno` | 失败时返回；子系统中止 `MakeCredential`。 |

<a id="gaeb4e348615069d77a81fb87c6970b640"></a>

### `fido2_get_state()`

```c
enum fido2_runtime_state fido2_get_state ( void )
```

```c
#include <zephyr/authentication/fido2/fido2.h>
```

获取 FIDO2 当前运行时状态（Runtime State）。

**说明（Note）**：注意（Note）：此函数可安全用于中断服务程序（ISR-safe）。

**返回（Returns）**：返回值（Returns）：当前运行时状态（Runtime State）。

<a id="ga020303d5fcc00471feba64eec8e169c2"></a>

### `fido2_init()`

```c
int fido2_init ( void )
```

```c
#include <zephyr/authentication/fido2/fido2.h>
```

初始化 FIDO2 子系统（Subsystem）。

设置凭据存储（Credential Storage）、密码功能（Crypto）和已注册传输（Registered Transports）。

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功时。 |
| `-errno` | 失败。 |

<a id="gaeb569aaa63c3c005d0df0b08c38896e1"></a>

### `fido2_reset()`

```c
int fido2_reset ( void )
```

```c
#include <zephyr/authentication/fido2/fido2.h>
```

执行恢复出厂设置（Factory Reset）。

清除所有已存储凭据（Credentials）和 PIN 状态，并重置认证器（Authenticator）。按照 CTAP2 规范，必须在上电后的 10 秒内执行。内部会强制执行此上电后 10 秒的时间窗口限制。

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功时。 |
| `-errno` | 失败。 |

<a id="gac2fecd9d7d18fbb8ff4b8e1083f86059"></a>

### `fido2_set_state_callback()`

```c
int fido2_set_state_callback ( fido2_state_callback_t cb, void * user_data )
```

```c
#include <zephyr/authentication/fido2/fido2.h>
```

设置或清除唯一的 FIDO2 运行时状态回调（Runtime State Callback）。

将 `cb` 设为 `NULL` 可清除回调（Callback）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `cb` | 回调函数（Callback Function）；传入 `NULL` 可禁用回调。 |
| `user_data` | 传递给 `cb` 的不透明上下文指针（Opaque Context Pointer）。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 始终成功（Always Succeeds）。 |

**说明（Note）**：注意（Note）：如果 `cb` 不为 `NULL`，会立即在调用者上下文（Caller Context）中调用它一次，并传入当前状态。

<a id="gae7a1b8c0bf42ee2a0c3de0bc54c4fa72"></a>

### `fido2_start()`

```c
int fido2_start ( void )
```

```c
#include <zephyr/authentication/fido2/fido2.h>
```

启动 FIDO2 认证器（Authenticator）。

开始在所有已启用的传输（Transports）上监听 CTAP2 命令。

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功时。 |
| `-errno` | 失败。 |

<a id="gab41b4d957882b8d6844316ec2f3ccc95"></a>

### `fido2_stop()`

```c
int fido2_stop ( void )
```

```c
#include <zephyr/authentication/fido2/fido2.h>
```

停止 FIDO2 认证器（Authenticator）。

停止所有传输（Transports）和处理线程（Processing Thread）。

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功时。 |
| `-errno` | 失败。 |

<a id="gaf6d50aa0022f56350a927149086d7838"></a>

### `fido2_up_cancel()`

```c
void fido2_up_cancel ( void )
```

```c
#include <zephyr/authentication/fido2/fido2_up.h>
```

取消尚未完成的用户在场等待（Pending User Presence Wait）。

从传输（Transport）收到取消命令（Cancel Command）时调用。

使用 `CONFIG_FIDO2_UP_CUSTOM` 时，由应用程序提供的实现不得阻塞（Block）。

<a id="gae7fb0da6d327ef0be220d32558ea6be2"></a>

### `fido2_up_reset()`

```c
void fido2_up_reset ( void )
```

```c
#include <zephyr/authentication/fido2/fido2_up.h>
```

为新请求（Request）重置用户在场状态（User-Presence State）。

开始新请求（Request）之前，清除待处理的取消状态（Cancellation）和用户在场状态（User-presence State）。

<a id="gab782d78847a38dd7aeac52a806879dfb"></a>

### `fido2_up_wait()`

```c
int fido2_up_wait ( void )
```

```c
#include <zephyr/authentication/fido2/fido2_up.h>
```

FIDO2 用户在场（User Presence）。

检查用户在场（User Presence）。

阻塞等待用户的实体操作（Physical User Gesture），最长等待 `CONFIG_FIDO2_UP_TIMEOUT_MS`。

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 已确认用户在场（User Presence Confirmed）。 |
| `-ETIMEDOUT` | 超时到期，未发生用户交互（User Interaction）。 |
| `-ECANCELED` | 用户交互（User Interaction）已取消。 |
| `-errno` | 其他失败（Other Failure）时。 |

<a id="ga27aa8972d17b4ee6454204d0ab527ed0"></a>

### `fido2_storage_backend`

```c
const struct fido2_storage_api fido2_storage_backend
```

声明属性：`extern`。

```c
#include <zephyr/authentication/fido2/fido2_storage.h>
```

FIDO2 存储后端实例（Storage Backend Instance）。

存储后端（Storage Backend）必须为此符号提供且只提供一个定义；存在多个定义将导致链接错误（Link Error）。


## 8.6\_原页交叉引用（Cross References）

- [fido2.h](../api_file_service_interface_reference/P020_zephyr__authentication__fido2__fido2.h_文件参考.md)
- [fido2_attestation.h](../api_file_service_reference/P013_zephyr__authentication__fido2__fido2_attestation.h_文件参考.md)
- [fido2_storage.h](../api_file_configuration_reference/P027_zephyr__authentication__fido2__fido2_storage.h_文件参考.md)
- [fido2_transport.h](../api_file_secure_value_reference/P008_zephyr__authentication__fido2__fido2_transport.h_文件参考.md)
- [fido2_types.h](../api_file_flash_test_reference/P002_zephyr__authentication__fido2__fido2_types.h_文件参考.md)
- [fido2_up.h](../api_file_runtime_reference/P015_zephyr__authentication__fido2__fido2_up.h_文件参考.md)
- [state](../api_file_reference/P291_zephyr__net__http__parser_state.h_文件参考.md#adc6e5733fc3c22f0a7b2914188c49c90)
- [BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)
- [fido2_credential](../platform_security_model_reference/P007_fido2_credential_结构体.md)
- [fido2_storage_api](../platform_security_model_reference/P009_fido2_storage_api_结构体.md)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [fido2_attestation_result](../platform_security_model_reference/P006_fido2_attestation_result_结构体.md)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="doc-typedef-members"></a>
<a id="header-doc-typedef-members"></a>
<a id="doc-enum-members"></a>
<a id="header-doc-enum-members"></a>
<a id="gaec9e2106f2d776266909f5e2baf924d9aca44c6fcf4ff9f7d43693607a4ea178a"></a>
<a id="gaec9e2106f2d776266909f5e2baf924d9a64758dfc5b08bccc58369e97ecd8eae0"></a>
<a id="gaec9e2106f2d776266909f5e2baf924d9a2419f886d7fcfe8e4e77a4b5f21d5bfc"></a>
<a id="gaec9e2106f2d776266909f5e2baf924d9a6b7d85b947ad93ab5159ffe7f2934948"></a>
<a id="gaec9e2106f2d776266909f5e2baf924d9aacffe603fa91c1102164c1d022bcd678"></a>
<a id="gaec9e2106f2d776266909f5e2baf924d9adc26ad4d923d58ca0f33d63c9dae1c27"></a>
<a id="gaec9e2106f2d776266909f5e2baf924d9a4984d83c6210b1855106ff39b413e614"></a>
<a id="gaec9e2106f2d776266909f5e2baf924d9a327a6fbfb22651dfed6d1d1ded574ab7"></a>
<a id="ga86aa0e78a95ea9e399c3831348fe8684a94ae94ce511d5898c12059766adf95c3"></a>
<a id="ga86aa0e78a95ea9e399c3831348fe8684a21d965a84070571fb2e0d475cf27043d"></a>
<a id="ga86aa0e78a95ea9e399c3831348fe8684a386cd8a5baf42b49b2271d655645b103"></a>
<a id="ga86aa0e78a95ea9e399c3831348fe8684ad2a327ca6649f0abd4153dee72952167"></a>
<a id="gae9411b5f6c2596cf49f7ebcf04fd7955a07603aa0b0598319d504ca9e23e76078"></a>
<a id="gae9411b5f6c2596cf49f7ebcf04fd7955a2299549abdae08cd0e71c7db3d918ca6"></a>
<a id="gae9411b5f6c2596cf49f7ebcf04fd7955aef0d3d870129fc9e72138d309c641be6"></a>
<a id="ggabf5068079e94310fb4b942df56ec1d10acc12ded1d9bd2a04d4b6346c186f8a67"></a>
<a id="ggabf5068079e94310fb4b942df56ec1d10a8c7700d3df270e15fc9e6cd0a536bd9a"></a>
<a id="ggabf5068079e94310fb4b942df56ec1d10ac1dcd5cc47e59480df023bcc6d239909"></a>
<a id="ggabf5068079e94310fb4b942df56ec1d10a64e677309cf5594b723f9b5c76e52774"></a>
<a id="ga6b3b79c7ef54b3ebbe686d4f67aaf7fcaa08efc6dee799b3e1fb8490bc64bd1cf"></a>
<a id="ga6b3b79c7ef54b3ebbe686d4f67aaf7fcab263ae4a933b875d54a86d4a6da8dc4e"></a>
<a id="ga6b3b79c7ef54b3ebbe686d4f67aaf7fcab4382a900e27d13b5043241f2f6dc2fe"></a>
<a id="ga6b3b79c7ef54b3ebbe686d4f67aaf7fcacbaf6656b7eac960f4bc0e561de47011"></a>
<a id="ga6b3b79c7ef54b3ebbe686d4f67aaf7fca809431ef12cd0ba7094a80c39d6bdc2d"></a>
<a id="ga6b3b79c7ef54b3ebbe686d4f67aaf7fcaf713403e6582ce02cace5d29f45405af"></a>
<a id="ga6b3b79c7ef54b3ebbe686d4f67aaf7fcac36b384a558597d72980f2425008c7b6"></a>
<a id="ga6b3b79c7ef54b3ebbe686d4f67aaf7fcacf7163e857eb9b8b6ddef1e7ff2b7351"></a>
<a id="ga6b3b79c7ef54b3ebbe686d4f67aaf7fca1ece48887496a5962823530201eaf48c"></a>
<a id="ga6b3b79c7ef54b3ebbe686d4f67aaf7fca17c4a70a8f87425c4d849585d28280d4"></a>
<a id="ga6b3b79c7ef54b3ebbe686d4f67aaf7fcac804a5a070c6552d89d403ffc953c00d"></a>
<a id="ga6b3b79c7ef54b3ebbe686d4f67aaf7fcad19e5127b17b8e0abee8bfe7d1ae595f"></a>
<a id="ga6b3b79c7ef54b3ebbe686d4f67aaf7fcaee29e086a2af8e697b6467c9667cb327"></a>
<a id="ga6b3b79c7ef54b3ebbe686d4f67aaf7fcabe9d8c984a0c0a62616a4a94af655a78"></a>
<a id="ga6b3b79c7ef54b3ebbe686d4f67aaf7fcacc4208f8ab39ba6b67c9358df6b88797"></a>
<a id="ga6b3b79c7ef54b3ebbe686d4f67aaf7fcaffdba1168067976851629c2111f46f6a"></a>
<a id="ga6b3b79c7ef54b3ebbe686d4f67aaf7fca5dfe38f41a7863bc04928d7c566568b7"></a>
<a id="ga6b3b79c7ef54b3ebbe686d4f67aaf7fca128911647928193e076041834e398e75"></a>
<a id="ga6b3b79c7ef54b3ebbe686d4f67aaf7fca4c53af9f0ad3e857bf86efea60b9370f"></a>
<a id="ga6b3b79c7ef54b3ebbe686d4f67aaf7fca8d108ee70faea78aa0669a90081dd05c"></a>
<a id="ga6b3b79c7ef54b3ebbe686d4f67aaf7fca020a5895146a35c2dedace5e0ff96112"></a>
<a id="ga6b3b79c7ef54b3ebbe686d4f67aaf7fca376b899ff97c4d39f201f20e03a36ed7"></a>
<a id="ga6b3b79c7ef54b3ebbe686d4f67aaf7fca3521d75934cddcd0d009279541381c41"></a>
<a id="ga6b3b79c7ef54b3ebbe686d4f67aaf7fca507f5ded749fdba95d6b16d859052d43"></a>
<a id="ga6b3b79c7ef54b3ebbe686d4f67aaf7fcacb6d4da143bbd72b7d361a7a4e38b1da"></a>
<a id="ga6b3b79c7ef54b3ebbe686d4f67aaf7fcaad5b849ccb37209d531444bb346e3158"></a>
<a id="ga6b3b79c7ef54b3ebbe686d4f67aaf7fca05bb5e1370a3e46ef1a2f2545cf5675c"></a>
<a id="ga6b3b79c7ef54b3ebbe686d4f67aaf7fca336c3e439e0a1b3eb24cf3edc38455e1"></a>
<a id="ga6b3b79c7ef54b3ebbe686d4f67aaf7fcafcbd15f2df2744ed0afd3613540ad6a3"></a>
<a id="ga6b3b79c7ef54b3ebbe686d4f67aaf7fca39355da927952f311dd8cdf9fe5cced8"></a>
<a id="ga6b3b79c7ef54b3ebbe686d4f67aaf7fca739a74cd005fc1b3b8853f7aa2db7e3e"></a>
<a id="ga6b3b79c7ef54b3ebbe686d4f67aaf7fca6eb4c3a5f51db1d0232ef8ca21d194e6"></a>
<a id="ga6b3b79c7ef54b3ebbe686d4f67aaf7fca05c0bff840ed8b7e85c147876792760f"></a>
<a id="ga6b3b79c7ef54b3ebbe686d4f67aaf7fca63548371fe576d03e00a2d428bf2501b"></a>
<a id="ga6b3b79c7ef54b3ebbe686d4f67aaf7fca57a9754a770796bdb303ec5503222060"></a>
<a id="ga6b3b79c7ef54b3ebbe686d4f67aaf7fcab59eee02a04da8ca4bf54ceba81794d0"></a>
<a id="ga6b3b79c7ef54b3ebbe686d4f67aaf7fca5c952ab01843550e24d3aa672f05fec9"></a>
<a id="ga6b3b79c7ef54b3ebbe686d4f67aaf7fca8406e112b928b9f556cced2f0c391cfe"></a>
<a id="ga6b3b79c7ef54b3ebbe686d4f67aaf7fca935a727495553c4bf584a92c39d780b7"></a>
<a id="ga6b3b79c7ef54b3ebbe686d4f67aaf7fca0ca1a5d18e501d446c58ddcc4f8fbc05"></a>
<a id="ga6b3b79c7ef54b3ebbe686d4f67aaf7fca356a92621e9d79fd5d599f1c13a7da93"></a>
<a id="ga6b3b79c7ef54b3ebbe686d4f67aaf7fcaa28ed4a202b7c8eca14a727b708b0d50"></a>
<a id="ga6b3b79c7ef54b3ebbe686d4f67aaf7fcaeb3d5db8b9e7ad3123df8d2a76ed4bfe"></a>
<a id="ga6b3b79c7ef54b3ebbe686d4f67aaf7fca43b6e71c8f000bb2eccfc8a45c4591d3"></a>
<a id="ga6b3b79c7ef54b3ebbe686d4f67aaf7fca53aa4e296d54d24d7aab0bfc7747d893"></a>
<a id="ga6b3b79c7ef54b3ebbe686d4f67aaf7fca620c7a76e1481401e9dce1a5a75c8ee8"></a>
<a id="ga6b3b79c7ef54b3ebbe686d4f67aaf7fca69c9ebc7f40bcc26641eaa910a84f7e4"></a>
<a id="ga6b3b79c7ef54b3ebbe686d4f67aaf7fcab52bc5933983ff9464292f4a470e0217"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>
<a id="doc-var-members"></a>
<a id="header-doc-var-members"></a>

---

[上一章](P007_以太网支持函数（Ethernet Support Functions）.md) · [返回大纲](大纲.md) · [下一章](P009_LoRa API主题.md)
