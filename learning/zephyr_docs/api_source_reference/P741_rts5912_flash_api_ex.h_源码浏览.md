---
id: learning.zephyr-docs.api-source-reference.page-741
title: rts5912_flash_api_ex.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/rts5912__flash__api__ex_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第741章\_rts5912\_flash\_api\_ex.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/rts5912__flash__api__ex_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/rts5912__flash__api__ex_8h.html)。

## 741.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
<a id="l00012"></a>
<a id="l00013"></a>
<a id="l00014"></a>
<a id="l00015"></a>
<a id="l00022"></a>
<a id="foldopen00026"></a>
<a id="l00026"></a>
<a id="l00036"></a>
<a id="l00037"></a>
<a id="l00047"></a>
<a id="l00048"></a>
<a id="l00058"></a>
<a id="l00059"></a>
<a id="l00069"></a>
<a id="l00070"></a>
<a id="l00080"></a>
<a id="l00081"></a>
<a id="l00091"></a>
<a id="l00092"></a>
<a id="l00103"></a>
<a id="l00104"></a>
<a id="l00116"></a>
<a id="l00117"></a>
<a id="l00118"></a>
<a id="l00122"></a>
<a id="l00123"></a>
<a id="agroup__flash__interface_html_ga67418b2d5cbbec83463dce3d426162e3"></a>
<a id="agroup__rts5912__flash__ex__op_html_ga76926a3c77ab9b717612e578b19ed839"></a>
<a id="agroup__rts5912__flash__ex__op_html_gga76926a3c77ab9b717612e578b19ed839a62b267b7e87b85c185cbe7dd846c7a2e"></a>
<a id="agroup__rts5912__flash__ex__op_html_gga76926a3c77ab9b717612e578b19ed839a8380795da4ba7f938d8ba1eaaf8a2614"></a>
<a id="agroup__rts5912__flash__ex__op_html_gga76926a3c77ab9b717612e578b19ed839a982b4c3e330184dc7a70d93d78f3673e"></a>
<a id="agroup__rts5912__flash__ex__op_html_gga76926a3c77ab9b717612e578b19ed839aba07d1e19388fb24dcc3b0b03ffd1695"></a>
<a id="agroup__rts5912__flash__ex__op_html_gga76926a3c77ab9b717612e578b19ed839abd2ecf801e42710d563e3edf08724f9c"></a>
<a id="agroup__rts5912__flash__ex__op_html_gga76926a3c77ab9b717612e578b19ed839acf8b81b0f577bf7916bbd9c71a01eab8"></a>
<a id="agroup__rts5912__flash__ex__op_html_gga76926a3c77ab9b717612e578b19ed839ad3a6db835d8651b5a428caf610d3cb0f"></a>
<a id="agroup__rts5912__flash__ex__op_html_gga76926a3c77ab9b717612e578b19ed839adf5f76fee83c48c041075aa6e3826584"></a>

```c
/*
 * Copyright (c) 2025 Realtek, SIBG-SD7
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_DRIVERS_FLASH_RTS5912_FLASH_API_EX_H_
#define ZEPHYR_INCLUDE_DRIVERS_FLASH_RTS5912_FLASH_API_EX_H_


enum flash_rts5912_ex_ops {
        FLASH_RTS5912_EX_OP_WR_ENABLE = FLASH_EX_OP_VENDOR_BASE,

        FLASH_RTS5912_EX_OP_WR_DISABLE,

        FLASH_RTS5912_EX_OP_WR_SR,

        FLASH_RTS5912_EX_OP_WR_SR2,

        FLASH_RTS5912_EX_OP_RD_SR,

        FLASH_RTS5912_EX_OP_RD_SR2,

        FLASH_RTS5912_EX_OP_SET_WP,

        FLASH_RTS5912_EX_OP_GET_WP,
};


#endif /* ZEPHYR_INCLUDE_DRIVERS_FLASH_RTS5912_FLASH_API_EX_H_ */
```

## 741.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2025 Realtek, SIBG-SD7。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 123 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DRIVERS_FLASH_RTS5912_FLASH_API_EX_H_`。

## 741.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/rts5912__flash__api__ex_8h.html)
- [flash_rts5912_ex_ops](https://docs.zephyrproject.org/latest/doxygen/html/group__rts5912__flash__ex__op.html#ga76926a3c77ab9b717612e578b19ed839)
- [FLASH_RTS5912_EX_OP_WR_ENABLE](https://docs.zephyrproject.org/latest/doxygen/html/group__rts5912__flash__ex__op.html#gga76926a3c77ab9b717612e578b19ed839acf8b81b0f577bf7916bbd9c71a01eab8)
- [FLASH_EX_OP_VENDOR_BASE](../flash_reference/P001_Flash公共接口.md#ga67418b2d5cbbec83463dce3d426162e3)
- [FLASH_RTS5912_EX_OP_WR_DISABLE](https://docs.zephyrproject.org/latest/doxygen/html/group__rts5912__flash__ex__op.html#gga76926a3c77ab9b717612e578b19ed839abd2ecf801e42710d563e3edf08724f9c)
- [FLASH_RTS5912_EX_OP_WR_SR](https://docs.zephyrproject.org/latest/doxygen/html/group__rts5912__flash__ex__op.html#gga76926a3c77ab9b717612e578b19ed839aba07d1e19388fb24dcc3b0b03ffd1695)
- [FLASH_RTS5912_EX_OP_WR_SR2](https://docs.zephyrproject.org/latest/doxygen/html/group__rts5912__flash__ex__op.html#gga76926a3c77ab9b717612e578b19ed839adf5f76fee83c48c041075aa6e3826584)
- [FLASH_RTS5912_EX_OP_RD_SR](https://docs.zephyrproject.org/latest/doxygen/html/group__rts5912__flash__ex__op.html#gga76926a3c77ab9b717612e578b19ed839a62b267b7e87b85c185cbe7dd846c7a2e)
- [FLASH_RTS5912_EX_OP_RD_SR2](https://docs.zephyrproject.org/latest/doxygen/html/group__rts5912__flash__ex__op.html#gga76926a3c77ab9b717612e578b19ed839ad3a6db835d8651b5a428caf610d3cb0f)
- [FLASH_RTS5912_EX_OP_SET_WP](https://docs.zephyrproject.org/latest/doxygen/html/group__rts5912__flash__ex__op.html#gga76926a3c77ab9b717612e578b19ed839a8380795da4ba7f938d8ba1eaaf8a2614)
- [FLASH_RTS5912_EX_OP_GET_WP](https://docs.zephyrproject.org/latest/doxygen/html/group__rts5912__flash__ex__op.html#gga76926a3c77ab9b717612e578b19ed839a982b4c3e330184dc7a70d93d78f3673e)

---

[上一章](P740_rts5817_reset.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P742_rv32m1-pinctrl.h_源码浏览.md)
