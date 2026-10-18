---
id: learning.zephyr-docs.api-file-service-interface-reference.page-17
title: zephyr__bluetooth__ead.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/ead_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第17章\_zephyr\_\_bluetooth\_\_ead.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/ead_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <stddef.h>
#include <stdint.h>
#include <zephyr/bluetooth/bluetooth.h>
#include <zephyr/kernel.h>
```

查看此文件的源码。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 17.1\_宏定义（Macros）

<a id="r_gae2de6773ee7179ab857f2d0eea168b88"></a>

```c
#define BT_EAD_RANDOMIZER_SIZE 5
```

相关声明：[BT_EAD_RANDOMIZER_SIZE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ead.html#gae2de6773ee7179ab857f2d0eea168b88)。

随机量（Randomizer）大小，单位为字节。

<a id="r_gab25e457cbc2f81738de82832f61e2353"></a>

```c
#define BT_EAD_KEY_SIZE 16
```

相关声明：[BT_EAD_KEY_SIZE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ead.html#gab25e457cbc2f81738de82832f61e2353)。

密钥（Key）大小，单位为字节。

<a id="r_ga03c2e091e276f522dd6ebbceadb56d72"></a>

```c
#define BT_EAD_IV_SIZE 8
```

相关声明：[BT_EAD_IV_SIZE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ead.html#ga03c2e091e276f522dd6ebbceadb56d72)。

初始化向量（Initialisation Vector）大小，单位为字节。

<a id="r_ga4f61690f24aae84871dfb461e2d32449"></a>

```c
#define BT_EAD_MIC_SIZE 4
```

相关声明：[BT_EAD_MIC_SIZE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ead.html#ga4f61690f24aae84871dfb461e2d32449)。

消息完整性校验码（MIC）大小，单位为字节。

<a id="r_ga82a48e03dbbffe0e82ca80941a34a2cb"></a>

```c
#define BT_EAD_ENCRYPTED_PAYLOAD_SIZE(payload_size)
```

相关声明：[BT_EAD_ENCRYPTED_PAYLOAD_SIZE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ead.html#ga82a48e03dbbffe0e82ca80941a34a2cb)。

根据给定的载荷字节数，获取加密广播数据（Encrypted Advertising Data）的大小，单位为字节。

<a id="r_ga9dbaf3919a0e47adb89e69ea7f3b89a2"></a>

```c
#define BT_EAD_DECRYPTED_PAYLOAD_SIZE(encrypted_payload_size)
```

相关声明：[BT_EAD_DECRYPTED_PAYLOAD_SIZE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ead.html#ga9dbaf3919a0e47adb89e69ea7f3b89a2)。

根据给定的载荷字节数，获取解密后载荷（Decrypted Payload）的大小，单位为字节。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 17.2\_函数（Functions）

<a id="r_ga8bed2f85d63b3950fd3e19fe211a8f02"></a>

```c
int bt_ead_encrypt (const uint8_t session_key[16], const uint8_t iv[8], const uint8_t *payload, size_t payload_size, uint8_t *encrypted_payload)
```

相关声明：[bt_ead_encrypt](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ead.html#ga8bed2f85d63b3950fd3e19fe211a8f02)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

加密并认证（Encrypt and Authenticate）指定的广播数据。

<a id="r_gaf4005550479008e5f32f5cf15200ea8e"></a>

```c
int bt_ead_decrypt (const uint8_t session_key[16], const uint8_t iv[8], const uint8_t *encrypted_payload, size_t encrypted_payload_size, uint8_t *payload)
```

相关声明：[bt_ead_decrypt](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ead.html#gaf4005550479008e5f32f5cf15200ea8e)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

解密并认证（Decrypt and Authenticate）指定的加密广播数据。


## 17.3\_原页交叉引用（Cross References）

- [stdint.h](../api_source_device_reference/P036_stdint.h_源码浏览.md)
- [zephyr/bluetooth/bluetooth.h](../api_source_system_reference/P003_bluetooth.h_源码浏览.md)
- [zephyr/kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h_source.html)
- [查看此文件的源码。](../api_source_reference/P217_ead.h_源码浏览.md)
- [BT_EAD_RANDOMIZER_SIZE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ead.html#gae2de6773ee7179ab857f2d0eea168b88)
- [BT_EAD_KEY_SIZE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ead.html#gab25e457cbc2f81738de82832f61e2353)
- [BT_EAD_IV_SIZE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ead.html#ga03c2e091e276f522dd6ebbceadb56d72)
- [BT_EAD_MIC_SIZE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ead.html#ga4f61690f24aae84871dfb461e2d32449)
- [BT_EAD_ENCRYPTED_PAYLOAD_SIZE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ead.html#ga82a48e03dbbffe0e82ca80941a34a2cb)
- [BT_EAD_DECRYPTED_PAYLOAD_SIZE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ead.html#ga9dbaf3919a0e47adb89e69ea7f3b89a2)
- [bt_ead_encrypt](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ead.html#ga8bed2f85d63b3950fd3e19fe211a8f02)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [bt_ead_decrypt](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ead.html#gaf4005550479008e5f32f5cf15200ea8e)

---

[上一章](P016_zephyr__dt-bindings__gpio__dvp-20pin-connector.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P018_zephyr__drivers__espi_emul.h_文件参考.md)
