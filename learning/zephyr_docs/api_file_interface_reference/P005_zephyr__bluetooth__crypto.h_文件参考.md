---
id: learning.zephyr-docs.api-file-interface-reference.page-5
title: zephyr__bluetooth__crypto.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/bluetooth_2crypto_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第5章\_zephyr\_\_bluetooth\_\_crypto.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/bluetooth_2crypto_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

蓝牙子系统（Bluetooth Subsystem）的密码API。

<a id="details"></a>

```c
#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>
```

查看此文件的源码。

蓝牙子系统（Bluetooth Subsystem）的密码API。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 5.1\_函数（Functions）

<a id="r_ga2c85d3563547017ae97f22993272fb29"></a>

```c
int bt_rand (void *buf, size_t len)
```

相关声明：[bt_rand](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__crypto.html#ga2c85d3563547017ae97f22993272fb29)。

生成随机数据（random data）。

<a id="r_ga54d34c154deaf5b6f1523de15ddec18f"></a>

```c
int bt_encrypt_le (const uint8_t key[16], const uint8_t plaintext[16], uint8_t enc_data[16])
```

相关声明：[bt_encrypt_le](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__crypto.html#ga54d34c154deaf5b6f1523de15ddec18f)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

对小端序（little-endian）数据进行 AES 加密。

<a id="r_gab93f5833e39b39e388bf40ba5c60d60f"></a>

```c
int bt_encrypt_be (const uint8_t key[16], const uint8_t plaintext[16], uint8_t enc_data[16])
```

相关声明：[bt_encrypt_be](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__crypto.html#gab93f5833e39b39e388bf40ba5c60d60f)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

对大端序（big-endian）数据进行 AES 加密。

<a id="r_ga413a29883453982f0da13590dd493166"></a>

```c
int bt_ccm_decrypt (const uint8_t key[16], uint8_t nonce[13], const uint8_t *enc_data, size_t len, const uint8_t *aad, size_t aad_len, uint8_t *plaintext, size_t mic_size)
```

相关声明：[bt_ccm_decrypt](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__crypto.html#ga413a29883453982f0da13590dd493166)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

使用 AES-CCM 解密大端序数据。

<a id="r_ga7235be4697031ca6a0e535bdd707d3e1"></a>

```c
int bt_ccm_encrypt (const uint8_t key[16], uint8_t nonce[13], const uint8_t *plaintext, size_t len, const uint8_t *aad, size_t aad_len, uint8_t *enc_data, size_t mic_size)
```

相关声明：[bt_ccm_encrypt](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__crypto.html#ga7235be4697031ca6a0e535bdd707d3e1)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

使用 AES-CCM 加密大端序数据。


## 5.2\_原页交叉引用（Cross References）

- [stdbool.h](../api_source_supplement_reference/P186_stdbool.h_源码浏览.md)
- [stdint.h](../api_source_device_reference/P036_stdint.h_源码浏览.md)
- [查看此文件的源码。](../api_source_reference/P072_crypto.h_源码浏览.md)
- [bt_rand](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__crypto.html#ga2c85d3563547017ae97f22993272fb29)
- [bt_encrypt_le](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__crypto.html#ga54d34c154deaf5b6f1523de15ddec18f)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [bt_encrypt_be](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__crypto.html#gab93f5833e39b39e388bf40ba5c60d60f)
- [bt_ccm_decrypt](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__crypto.html#ga413a29883453982f0da13590dd493166)
- [bt_ccm_encrypt](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__crypto.html#ga7235be4697031ca6a0e535bdd707d3e1)

<a id="header-details"></a>

---

[上一章](P004_zephyr__dt-bindings__sensor__adxl372.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P006_zephyr__mgmt__mcumgr__mgmt__callback_defines.h_文件参考.md)
