---
id: learning.zephyr-docs.api-source-reference.page-85
title: ccid.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/ccid_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第85章\_ccid.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/ccid_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/ccid_8h.html)。

## 85.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00010"></a>
<a id="l00011"></a>
<a id="l00012"></a>
<a id="l00013"></a>
<a id="l00026"></a>
<a id="l00027"></a>
<a id="l00028"></a>
<a id="l00029"></a>
<a id="l00030"></a>
<a id="l00031"></a>
<a id="l00032"></a>
<a id="l00033"></a>
<a id="l00034"></a>
<a id="l00036"></a>
<a id="l00038"></a>
<a id="l00039"></a>
<a id="l00052"></a>
<a id="l00053"></a>
<a id="l00066"></a>
<a id="l00067"></a>
<a id="l00069"></a>
<a id="l00070"></a>
<a id="l00071"></a>
<a id="l00072"></a>
<a id="l00073"></a>
<a id="l00074"></a>
<a id="agatt_8h_html"></a>
<a id="agroup__bt__ccid_html_ga07845fe5cc445a35448881430f528609"></a>
<a id="agroup__bt__ccid_html_gad621dd750e4b1c23791afc72785990fc"></a>
<a id="astdint_8h_html"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="astructbt__gatt__attr_html"></a>

```c


#ifndef ZEPHYR_INCLUDE_BLUETOOTH_AUDIO_CCID_H_
#define ZEPHYR_INCLUDE_BLUETOOTH_AUDIO_CCID_H_


#include <stdint.h>

#include <zephyr/bluetooth/gatt.h>

#ifdef __cplusplus
extern "C" {
#endif

#define BT_CCID_MIN 0U
#define BT_CCID_MAX 255U

int bt_ccid_alloc_value(void);

const struct bt_gatt_attr *bt_ccid_find_attr(uint8_t ccid);


#ifdef __cplusplus
}
#endif

#endif /* ZEPHYR_INCLUDE_BLUETOOTH_AUDIO_CCID_H_ */
```

## 85.2\_可见注释译文（Comments）

### 注释 1：原第 74 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_BLUETOOTH_AUDIO_CCID_H_`。

## 85.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/ccid_8h.html)
- [stdint.h](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html)
- [zephyr/bluetooth/gatt.h](https://docs.zephyrproject.org/latest/doxygen/html/gatt_8h.html)
- [bt_ccid_alloc_value](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ccid.html#gad621dd750e4b1c23791afc72785990fc)
- [bt_gatt_attr](../bluetooth_connection_model_reference/P049_bt_gatt_attr_结构体.md)
- [bt_ccid_find_attr](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ccid.html#ga07845fe5cc445a35448881430f528609)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [gatt.h](https://docs.zephyrproject.org/latest/doxygen/html/gatt_8h.html)

---

[上一章](P084_can_fake.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P086_cdefs.h_源码浏览.md)
