---
id: learning.zephyr-docs.api-source-reference.page-217
title: ead.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/ead_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第217章\_ead.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/ead_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/ead_8h.html)。

## 217.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
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
<a id="l00014"></a>
<a id="l00015"></a>
<a id="l00016"></a>
<a id="l00017"></a>
<a id="l00024"></a>
<a id="l00026"></a>
<a id="l00028"></a>
<a id="l00030"></a>
<a id="l00032"></a>
<a id="l00033"></a>
<a id="foldopen00037"></a>
<a id="l00037"></a>
<a id="l00038"></a>
<a id="l00039"></a>
<a id="foldopen00043"></a>
<a id="l00043"></a>
<a id="l00044"></a>
<a id="l00045"></a>
<a id="l00077"></a>
<a id="l00078"></a>
<a id="l00079"></a>
<a id="l00103"></a>
<a id="l00104"></a>
<a id="l00105"></a>
<a id="l00106"></a>
<a id="l00110"></a>
<a id="l00111"></a>
<a id="l00112"></a>
<a id="l00113"></a>
<a id="l00114"></a>
<a id="l00115"></a>
<a id="abluetooth_2bluetooth_8h_html"></a>
<a id="agroup__bt__ead_html_ga03c2e091e276f522dd6ebbceadb56d72"></a>
<a id="agroup__bt__ead_html_ga8bed2f85d63b3950fd3e19fe211a8f02"></a>
<a id="agroup__bt__ead_html_gab25e457cbc2f81738de82832f61e2353"></a>
<a id="agroup__bt__ead_html_gaf4005550479008e5f32f5cf15200ea8e"></a>
<a id="akernel_8h_html"></a>
<a id="astdint_8h_html"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>

```c
/* Copyright (c) 2023 Nordic Semiconductor ASA
 * SPDX-License-Identifier: Apache-2.0
 */

#include <stddef.h>
#include <stdint.h>

#ifndef ZEPHYR_INCLUDE_BLUETOOTH_EAD_H_
#define ZEPHYR_INCLUDE_BLUETOOTH_EAD_H_

#include <zephyr/bluetooth/bluetooth.h>
#include <zephyr/kernel.h>

#ifdef __cplusplus
extern "C" {
#endif


#define BT_EAD_RANDOMIZER_SIZE 5
#define BT_EAD_KEY_SIZE        16
#define BT_EAD_IV_SIZE         8
#define BT_EAD_MIC_SIZE        4

#define BT_EAD_ENCRYPTED_PAYLOAD_SIZE(payload_size)                                                \
        ((payload_size) + BT_EAD_RANDOMIZER_SIZE + BT_EAD_MIC_SIZE)

#define BT_EAD_DECRYPTED_PAYLOAD_SIZE(encrypted_payload_size)                                      \
        ((encrypted_payload_size) - (BT_EAD_RANDOMIZER_SIZE + BT_EAD_MIC_SIZE))

int bt_ead_encrypt(const uint8_t session_key[BT_EAD_KEY_SIZE], const uint8_t iv[BT_EAD_IV_SIZE],
                   const uint8_t *payload, size_t payload_size, uint8_t *encrypted_payload);

int bt_ead_decrypt(const uint8_t session_key[BT_EAD_KEY_SIZE], const uint8_t iv[BT_EAD_IV_SIZE],
                   const uint8_t *encrypted_payload, size_t encrypted_payload_size,
                   uint8_t *payload);


#ifdef __cplusplus
}
#endif

#endif /* ZEPHYR_INCLUDE_BLUETOOTH_EAD_H_ */
```

## 217.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2023 Nordic Semiconductor ASA。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 115 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_BLUETOOTH_EAD_H_`。

## 217.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/ead_8h.html)
- [stdint.h](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html)
- [zephyr/bluetooth/bluetooth.h](https://docs.zephyrproject.org/latest/doxygen/html/bluetooth_2bluetooth_8h.html)
- [zephyr/kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h.html)
- [bt_ead_encrypt](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ead.html#ga8bed2f85d63b3950fd3e19fe211a8f02)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [BT_EAD_KEY_SIZE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ead.html#gab25e457cbc2f81738de82832f61e2353)
- [BT_EAD_IV_SIZE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ead.html#ga03c2e091e276f522dd6ebbceadb56d72)
- [bt_ead_decrypt](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ead.html#gaf4005550479008e5f32f5cf15200ea8e)
- [bluetooth.h](https://docs.zephyrproject.org/latest/doxygen/html/bluetooth_2bluetooth_8h.html)
- [kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h.html)

---

[上一章](P216_dw_ace.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P218_ed2208-gca.h_源码浏览.md)
