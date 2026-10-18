---
id: learning.zephyr-docs.api-file-supplement-reference.page-103
title: zephyr__drivers__flash__rts5912_flash_api_ex.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/rts5912__flash__api__ex_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第103章\_zephyr\_\_drivers\_\_flash\_\_rts5912\_flash\_api\_ex.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/rts5912__flash__api__ex_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

Realtek RTS5912闪存扩展操作（Flash Extended Operations）的头文件。

查看此文件的源码。

<a id="details"></a>

Realtek RTS5912闪存扩展操作（Flash Extended Operations）的头文件。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 103.1\_枚举（Enumerations）

<a id="r_ga76926a3c77ab9b717612e578b19ed839"></a>

```c
enum flash_rts5912_ex_ops { FLASH_RTS5912_EX_OP_WR_ENABLE = FLASH_EX_OP_VENDOR_BASE , FLASH_RTS5912_EX_OP_WR_DISABLE , FLASH_RTS5912_EX_OP_WR_SR , FLASH_RTS5912_EX_OP_WR_SR2 , FLASH_RTS5912_EX_OP_RD_SR , FLASH_RTS5912_EX_OP_RD_SR2 , FLASH_RTS5912_EX_OP_SET_WP , FLASH_RTS5912_EX_OP_GET_WP }
```

相关声明：[flash_rts5912_ex_ops](https://docs.zephyrproject.org/latest/doxygen/html/group__rts5912__flash__ex__op.html#ga76926a3c77ab9b717612e578b19ed839)、[FLASH_RTS5912_EX_OP_WR_ENABLE](https://docs.zephyrproject.org/latest/doxygen/html/group__rts5912__flash__ex__op.html#gga76926a3c77ab9b717612e578b19ed839acf8b81b0f577bf7916bbd9c71a01eab8)、[FLASH_RTS5912_EX_OP_WR_DISABLE](https://docs.zephyrproject.org/latest/doxygen/html/group__rts5912__flash__ex__op.html#gga76926a3c77ab9b717612e578b19ed839abd2ecf801e42710d563e3edf08724f9c)、[FLASH_RTS5912_EX_OP_WR_SR](https://docs.zephyrproject.org/latest/doxygen/html/group__rts5912__flash__ex__op.html#gga76926a3c77ab9b717612e578b19ed839aba07d1e19388fb24dcc3b0b03ffd1695)、[FLASH_RTS5912_EX_OP_WR_SR2](https://docs.zephyrproject.org/latest/doxygen/html/group__rts5912__flash__ex__op.html#gga76926a3c77ab9b717612e578b19ed839adf5f76fee83c48c041075aa6e3826584)、[FLASH_RTS5912_EX_OP_RD_SR](https://docs.zephyrproject.org/latest/doxygen/html/group__rts5912__flash__ex__op.html#gga76926a3c77ab9b717612e578b19ed839a62b267b7e87b85c185cbe7dd846c7a2e)、[FLASH_RTS5912_EX_OP_RD_SR2](https://docs.zephyrproject.org/latest/doxygen/html/group__rts5912__flash__ex__op.html#gga76926a3c77ab9b717612e578b19ed839ad3a6db835d8651b5a428caf610d3cb0f)、[FLASH_RTS5912_EX_OP_SET_WP](https://docs.zephyrproject.org/latest/doxygen/html/group__rts5912__flash__ex__op.html#gga76926a3c77ab9b717612e578b19ed839a8380795da4ba7f938d8ba1eaaf8a2614)、[FLASH_RTS5912_EX_OP_GET_WP](https://docs.zephyrproject.org/latest/doxygen/html/group__rts5912__flash__ex__op.html#gga76926a3c77ab9b717612e578b19ed839a982b4c3e330184dc7a70d93d78f3673e)。

Realtek RTS5912 闪存扩展操作（Flash Extended Operations）的枚举（Enumeration）。


## 103.2\_原页交叉引用（Cross References）

- [查看此文件的源码。](../api_source_reference/P741_rts5912_flash_api_ex.h_源码浏览.md)
- [flash_rts5912_ex_ops](https://docs.zephyrproject.org/latest/doxygen/html/group__rts5912__flash__ex__op.html#ga76926a3c77ab9b717612e578b19ed839)
- [FLASH_RTS5912_EX_OP_WR_ENABLE](https://docs.zephyrproject.org/latest/doxygen/html/group__rts5912__flash__ex__op.html#gga76926a3c77ab9b717612e578b19ed839acf8b81b0f577bf7916bbd9c71a01eab8)
- [FLASH_RTS5912_EX_OP_WR_DISABLE](https://docs.zephyrproject.org/latest/doxygen/html/group__rts5912__flash__ex__op.html#gga76926a3c77ab9b717612e578b19ed839abd2ecf801e42710d563e3edf08724f9c)
- [FLASH_RTS5912_EX_OP_WR_SR](https://docs.zephyrproject.org/latest/doxygen/html/group__rts5912__flash__ex__op.html#gga76926a3c77ab9b717612e578b19ed839aba07d1e19388fb24dcc3b0b03ffd1695)
- [FLASH_RTS5912_EX_OP_WR_SR2](https://docs.zephyrproject.org/latest/doxygen/html/group__rts5912__flash__ex__op.html#gga76926a3c77ab9b717612e578b19ed839adf5f76fee83c48c041075aa6e3826584)
- [FLASH_RTS5912_EX_OP_RD_SR](https://docs.zephyrproject.org/latest/doxygen/html/group__rts5912__flash__ex__op.html#gga76926a3c77ab9b717612e578b19ed839a62b267b7e87b85c185cbe7dd846c7a2e)
- [FLASH_RTS5912_EX_OP_RD_SR2](https://docs.zephyrproject.org/latest/doxygen/html/group__rts5912__flash__ex__op.html#gga76926a3c77ab9b717612e578b19ed839ad3a6db835d8651b5a428caf610d3cb0f)
- [FLASH_RTS5912_EX_OP_SET_WP](https://docs.zephyrproject.org/latest/doxygen/html/group__rts5912__flash__ex__op.html#gga76926a3c77ab9b717612e578b19ed839a8380795da4ba7f938d8ba1eaaf8a2614)
- [FLASH_RTS5912_EX_OP_GET_WP](https://docs.zephyrproject.org/latest/doxygen/html/group__rts5912__flash__ex__op.html#gga76926a3c77ab9b717612e578b19ed839a982b4c3e330184dc7a70d93d78f3673e)

<a id="header-details"></a>

---

[上一章](P102_zephyr__dt-bindings__dma__rtl87x2g-dma.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P104_zephyr__drivers__sensor__s9706.h_文件参考.md)
