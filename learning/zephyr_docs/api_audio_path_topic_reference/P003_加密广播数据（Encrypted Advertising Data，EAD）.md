---
id: learning.zephyr-docs.api-audio-path-topic-reference.page-3
title: 加密广播数据（Encrypted Advertising Data，EAD）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ead.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第3章\_加密广播数据（Encrypted Advertising Data，EAD）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ead.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

加密广播数据（Encrypted Advertising Data，EAD）

<a id="details"></a>

加密广播数据（Encrypted Advertising Data，EAD）

<a id="header-define-members"></a>
<a id="define-members"></a>

## 3.1\_宏定义（Macros）

<a id="r_gae2de6773ee7179ab857f2d0eea168b88"></a>

```c
#define BT_EAD_RANDOMIZER_SIZE 5
```

相关声明：[BT_EAD_RANDOMIZER_SIZE](#gae2de6773ee7179ab857f2d0eea168b88)。

随机量（Randomizer）大小，单位为字节。

<a id="r_gab25e457cbc2f81738de82832f61e2353"></a>

```c
#define BT_EAD_KEY_SIZE 16
```

相关声明：[BT_EAD_KEY_SIZE](#gab25e457cbc2f81738de82832f61e2353)。

密钥（Key）大小，单位为字节。

<a id="r_ga03c2e091e276f522dd6ebbceadb56d72"></a>

```c
#define BT_EAD_IV_SIZE 8
```

相关声明：[BT_EAD_IV_SIZE](#ga03c2e091e276f522dd6ebbceadb56d72)。

初始化向量（Initialisation Vector）大小，单位为字节。

<a id="r_ga4f61690f24aae84871dfb461e2d32449"></a>

```c
#define BT_EAD_MIC_SIZE 4
```

相关声明：[BT_EAD_MIC_SIZE](#ga4f61690f24aae84871dfb461e2d32449)。

消息完整性校验码（MIC）大小，单位为字节。

<a id="r_ga82a48e03dbbffe0e82ca80941a34a2cb"></a>

```c
#define BT_EAD_ENCRYPTED_PAYLOAD_SIZE(payload_size)
```

相关声明：[BT_EAD_ENCRYPTED_PAYLOAD_SIZE](#ga82a48e03dbbffe0e82ca80941a34a2cb)。

根据给定的载荷字节数，获取加密广播数据（Encrypted Advertising Data）的大小，单位为字节。

<a id="r_ga9dbaf3919a0e47adb89e69ea7f3b89a2"></a>

```c
#define BT_EAD_DECRYPTED_PAYLOAD_SIZE(encrypted_payload_size)
```

相关声明：[BT_EAD_DECRYPTED_PAYLOAD_SIZE](#ga9dbaf3919a0e47adb89e69ea7f3b89a2)。

根据给定的载荷字节数，获取解密后载荷（Decrypted Payload）的大小，单位为字节。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 3.2\_函数（Functions）

<a id="r_ga8bed2f85d63b3950fd3e19fe211a8f02"></a>

```c
int bt_ead_encrypt (const uint8_t session_key[16], const uint8_t iv[8], const uint8_t *payload, size_t payload_size, uint8_t *encrypted_payload)
```

相关声明：[bt_ead_encrypt](#ga8bed2f85d63b3950fd3e19fe211a8f02)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

加密并认证（Encrypt and Authenticate）指定的广播数据。

<a id="r_gaf4005550479008e5f32f5cf15200ea8e"></a>

```c
int bt_ead_decrypt (const uint8_t session_key[16], const uint8_t iv[8], const uint8_t *encrypted_payload, size_t encrypted_payload_size, uint8_t *payload)
```

相关声明：[bt_ead_decrypt](#gaf4005550479008e5f32f5cf15200ea8e)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

解密并认证（Decrypt and Authenticate）指定的加密广播数据。

## 3.3\_详细说明（Detailed Documentation）

<a id="ga9dbaf3919a0e47adb89e69ea7f3b89a2"></a>

### `BT_EAD_DECRYPTED_PAYLOAD_SIZE`

```c
#define BT_EAD_DECRYPTED_PAYLOAD_SIZE ( encrypted_payload_size)
```

```c
#include <zephyr/bluetooth/ead.h>
```

展开值（Value）：

```c
((encrypted_payload_size) - (BT_EAD_RANDOMIZER_SIZE + BT_EAD_MIC_SIZE))
```

根据给定的载荷字节数，获取解密后载荷（Decrypted Payload）的大小，单位为字节。

<a id="ga82a48e03dbbffe0e82ca80941a34a2cb"></a>

### `BT_EAD_ENCRYPTED_PAYLOAD_SIZE`

```c
#define BT_EAD_ENCRYPTED_PAYLOAD_SIZE ( payload_size)
```

```c
#include <zephyr/bluetooth/ead.h>
```

展开值（Value）：

```c
((payload_size) + BT_EAD_RANDOMIZER_SIZE + BT_EAD_MIC_SIZE)
```

根据给定的载荷字节数，获取加密广播数据（Encrypted Advertising Data）的大小，单位为字节。

<a id="ga03c2e091e276f522dd6ebbceadb56d72"></a>

### `BT_EAD_IV_SIZE`

```c
#define BT_EAD_IV_SIZE 8
```

```c
#include <zephyr/bluetooth/ead.h>
```

初始化向量（Initialisation Vector）大小，单位为字节。

<a id="gab25e457cbc2f81738de82832f61e2353"></a>

### `BT_EAD_KEY_SIZE`

```c
#define BT_EAD_KEY_SIZE 16
```

```c
#include <zephyr/bluetooth/ead.h>
```

密钥（Key）大小，单位为字节。

<a id="ga4f61690f24aae84871dfb461e2d32449"></a>

### `BT_EAD_MIC_SIZE`

```c
#define BT_EAD_MIC_SIZE 4
```

```c
#include <zephyr/bluetooth/ead.h>
```

消息完整性校验码（MIC）大小，单位为字节。

<a id="gae2de6773ee7179ab857f2d0eea168b88"></a>

### `BT_EAD_RANDOMIZER_SIZE`

```c
#define BT_EAD_RANDOMIZER_SIZE 5
```

```c
#include <zephyr/bluetooth/ead.h>
```

随机量（Randomizer）大小，单位为字节。

<a id="gaf4005550479008e5f32f5cf15200ea8e"></a>

### `bt_ead_decrypt()`

```c
int bt_ead_decrypt ( const uint8_t session_key[16], const uint8_t iv[8], const uint8_t * encrypted_payload, size_t encrypted_payload_size, uint8_t * payload )
```

```c
#include <zephyr/bluetooth/ead.h>
```

解密并认证（Decrypt and Authenticate）指定的加密广播数据。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] session_key` | 用于加密的 16 字节密钥（Key）。 |
| `[in] iv` | 用于生成一次性数值（Nonce）的初始化向量（Initialisation Vector）。 |
| `[in] encrypted_payload` | 收到的加密广播数据（Encrypted Advertising Data）。仅应包含接收的广播结构中的广播数据，不包含长度或类型。 |
| `[in] encrypted_payload_size` | 接收到的广播数据大小，单位为字节。应等于接收的广播结构的长度字段值减去类型字段大小，即减去 1 字节。 |
| `[out] payload` | 解密后的广播有效载荷（Decrypted Advertising Payload）。使用 `BT_EAD_DECRYPTED_PAYLOAD_SIZE` 获取正确大小。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 数据已正确解密并通过认证（Decrypted and Authenticated）。 |
| `-EIO` | 解密或认证（Decryption or Authentication）期间发生错误。 |
| `-EINVAL` | 某个参数是 `NULL` 指针，或者 `encrypted_payload_size` 小于 `BT_EAD_RANDOMIZER_SIZE + BT_EAD_MIC_SIZE`。 |

**说明（Note）**：注意：广播结构（Advertising Structure）一词指广播数据、广播类型，以及这两部分的长度字段。

<a id="ga8bed2f85d63b3950fd3e19fe211a8f02"></a>

### `bt_ead_encrypt()`

```c
int bt_ead_encrypt ( const uint8_t session_key[16], const uint8_t iv[8], const uint8_t * payload, size_t payload_size, uint8_t * encrypted_payload )
```

```c
#include <zephyr/bluetooth/ead.h>
```

加密并认证（Encrypt and Authenticate）指定的广播数据。

`encrypted_payload` 中的结果数据布局如下：

- 随机化字段（Randomizer）放在起始的 `BT_EAD_RANDOMIZER_SIZE` 字节；
- 随后放入加密有效载荷（Encrypted Payload），共 `payload_size` 字节；
- 消息完整性检查值（MIC）放在最后的 `BT_EAD_MIC_SIZE` 字节。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] session_key` | 用于加密的密钥（Key），长度为 `BT_EAD_KEY_SIZE` 字节。 |
| `[in] iv` | 用于生成 nonce 的初始化向量（Initialisation Vector）。每当会话密钥（Session Key）改变时，它也必须改变。 |
| `[in] payload` | 要加密的广播数据（Advertising Data），可以由多个广播结构拼接而成。 |
| `[in] payload_size` | 要加密的广播数据大小（Advertising Data Size）。 |
| `[out] encrypted_payload` | 加密广播数据（Encrypted Ad Data），包含随机化字段（Randomizer）和消息完整性检查值（MIC）。大小至少为 `BT_EAD_RANDOMIZER_SIZE + payload_size + BT_EAD_MIC_SIZE`。使用 `BT_EAD_ENCRYPTED_PAYLOAD_SIZE` 获取正确大小。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 数据已正确加密并完成认证（Encrypted and Authenticated）。 |
| `-EIO` | 加密或认证（Encryption or Authentication）期间发生错误。 |
| `-EINVAL` | 某个参数是 `NULL` 指针。 |
| `-ECANCELED` | 随机数生成（Random Number Generation）期间发生错误。 |

**注意（Attention）**：注意：每次更新可解析私有地址（RPA），或修改数据时，都必须调用此函数。

**说明（Note）**：注意：广播结构（Advertising Structure）一词指广播数据、广播类型，以及这两部分的长度字段。


## 3.4\_原页交叉引用（Cross References）

- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [zephyr/bluetooth/ead.h](../api_file_service_interface_reference/P017_zephyr__bluetooth__ead.h_文件参考.md)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="agroup__bt__ead_html_ga4f61690f24aae84871dfb461e2d32449"></a>
<a id="agroup__bt__ead_html_gae2de6773ee7179ab857f2d0eea168b88"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P002_BAP 广播接收端 API（Broadcast Sink APIs）.md) · [返回大纲](大纲.md) · [下一章](P004_用于基本速率_增强数据速率（BR_EDR）的蓝牙逻辑链路控制与适配协议（Logical Link Control and Adaptation Protocol，L2CAP）。.md)
