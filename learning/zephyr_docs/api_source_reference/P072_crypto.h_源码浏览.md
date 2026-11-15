---
id: learning.zephyr-docs.api-source-reference.page-72
title: crypto.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/bluetooth_2crypto_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第72章\_crypto.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/bluetooth_2crypto_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/bluetooth_2crypto_8h.html)。

## 72.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
<a id="l00007"></a>
<a id="l00008"></a>
<a id="l00009"></a>
<a id="l00010"></a>
<a id="l00011"></a>
<a id="l00012"></a>
<a id="l00013"></a>
<a id="l00022"></a>
<a id="l00023"></a>
<a id="l00024"></a>
<a id="l00025"></a>
<a id="l00026"></a>
<a id="l00027"></a>
<a id="l00028"></a>
<a id="l00029"></a>
<a id="l00030"></a>
<a id="l00042"></a>
<a id="l00043"></a>
<a id="l00056"></a>
<a id="l00057"></a>
<a id="l00058"></a>
<a id="l00071"></a>
<a id="l00072"></a>
<a id="l00073"></a>
<a id="l00074"></a>
<a id="l00095"></a>
<a id="l00096"></a>
<a id="l00097"></a>
<a id="l00098"></a>
<a id="l00099"></a>
<a id="l00119"></a>
<a id="l00120"></a>
<a id="l00121"></a>
<a id="l00122"></a>
<a id="l00123"></a>
<a id="l00124"></a>
<a id="l00125"></a>
<a id="l00129"></a>
<a id="l00130"></a>
<a id="agroup__bt__crypto_html_ga2c85d3563547017ae97f22993272fb29"></a>
<a id="agroup__bt__crypto_html_ga413a29883453982f0da13590dd493166"></a>
<a id="agroup__bt__crypto_html_ga54d34c154deaf5b6f1523de15ddec18f"></a>
<a id="agroup__bt__crypto_html_ga7235be4697031ca6a0e535bdd707d3e1"></a>
<a id="agroup__bt__crypto_html_gab93f5833e39b39e388bf40ba5c60d60f"></a>
<a id="astdbool_8h_html"></a>
<a id="astdint_8h_html"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>

```c


/*
 * Copyright (c) 2017-2020 Nordic Semiconductor ASA
 * Copyright (c) 2015-2017 Intel Corporation
 *
 * SPDX-License-Identifier: Apache-2.0
 */
#ifndef ZEPHYR_INCLUDE_BLUETOOTH_CRYPTO_H_
#define ZEPHYR_INCLUDE_BLUETOOTH_CRYPTO_H_


#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>

#ifdef __cplusplus
extern "C" {
#endif

int bt_rand(void *buf, size_t len);

int bt_encrypt_le(const uint8_t key[16], const uint8_t plaintext[16],
                  uint8_t enc_data[16]);

int bt_encrypt_be(const uint8_t key[16], const uint8_t plaintext[16],
                  uint8_t enc_data[16]);


int bt_ccm_decrypt(const uint8_t key[16], uint8_t nonce[13], const uint8_t *enc_data,
                   size_t len, const uint8_t *aad, size_t aad_len,
                   uint8_t *plaintext, size_t mic_size);


int bt_ccm_encrypt(const uint8_t key[16], uint8_t nonce[13],
                   const uint8_t *plaintext, size_t len, const uint8_t *aad,
                   size_t aad_len, uint8_t *enc_data, size_t mic_size);

#ifdef __cplusplus
}
#endif

#endif /* ZEPHYR_INCLUDE_BLUETOOTH_CRYPTO_H_ */
```

## 72.2\_可见注释译文（Comments）

### 注释 1：原第 5 行

版权（Copyright）：© 2017-2020 Nordic Semiconductor ASA。

版权（Copyright）：© 2015-2017 Intel Corporation。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 130 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_BLUETOOTH_CRYPTO_H_`。

## 72.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/bluetooth_2crypto_8h.html)
- [stdbool.h](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html)
- [stdint.h](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html)
- [bt_rand](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__crypto.html#ga2c85d3563547017ae97f22993272fb29)
- [bt_encrypt_le](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__crypto.html#ga54d34c154deaf5b6f1523de15ddec18f)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [bt_encrypt_be](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__crypto.html#gab93f5833e39b39e388bf40ba5c60d60f)
- [bt_ccm_decrypt](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__crypto.html#ga413a29883453982f0da13590dd493166)
- [bt_ccm_encrypt](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__crypto.html#ga7235be4697031ca6a0e535bdd707d3e1)

---

[上一章](P071_controller.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P073_keys.h_源码浏览.md)
