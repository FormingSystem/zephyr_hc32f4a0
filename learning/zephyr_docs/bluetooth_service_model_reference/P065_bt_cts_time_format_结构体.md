---
id: learning.zephyr-docs.bluetooth-service-model-reference.page-65
title: bt_cts_time_format_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__cts__time__format.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第65章\_bt\_cts\_time\_format\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__cts__time__format.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

当前时间服务（Current Time Service）的数据格式，详细信息参见相应规范。

```c
#include <zephyr/bluetooth/services/cts.h>
```

<a id="details"></a>

当前时间服务（Current Time Service）的数据格式，详细信息参见相应规范。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 65.1\_数据成员（Data Fields）

<a id="r_ad5ab55fcb3e1dbaa73ba4ecb78d6b47e"></a>

```c
uint16_t year
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[year](#ad5ab55fcb3e1dbaa73ba4ecb78d6b47e)。

<a id="r_a079a1c49698b6e9cb84291acdd1cf687"></a>

```c
uint8_t mon
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[mon](#a079a1c49698b6e9cb84291acdd1cf687)。

<a id="r_a408a2b777d10b536dbdfeca1b8335e6b"></a>

```c
uint8_t mday
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[mday](#a408a2b777d10b536dbdfeca1b8335e6b)。

<a id="r_ab592c89e81e5cb43724affd3ce2b5768"></a>

```c
uint8_t hours
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[hours](#ab592c89e81e5cb43724affd3ce2b5768)。

<a id="r_a299d6432d9b44b0de0be9c130733eb69"></a>

```c
uint8_t min
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[min](#a299d6432d9b44b0de0be9c130733eb69)。

<a id="r_ae0ccd07b2a280888f3881f0d2fc2add6"></a>

```c
uint8_t sec
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[sec](#ae0ccd07b2a280888f3881f0d2fc2add6)。

<a id="r_ae696cbbd3a785c1df6d54ce771f1d7a2"></a>

```c
uint8_t wday
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[wday](#ae696cbbd3a785c1df6d54ce771f1d7a2)。

<a id="r_af601779a164440fe95c0dcbd7a3d7e60"></a>

```c
uint8_t fractions256
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[fractions256](#af601779a164440fe95c0dcbd7a3d7e60)。

<a id="r_a3482e00650e9e9a63816709c82a1aa07"></a>

```c
uint8_t reason
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[reason](#a3482e00650e9e9a63816709c82a1aa07)。

## 65.2\_详细说明（Detailed Documentation）

<a id="af601779a164440fe95c0dcbd7a3d7e60"></a>

### `fractions256`

```c
uint8_t bt_cts_time_format::fractions256
```

<a id="ab592c89e81e5cb43724affd3ce2b5768"></a>

### `hours`

```c
uint8_t bt_cts_time_format::hours
```

<a id="a408a2b777d10b536dbdfeca1b8335e6b"></a>

### `mday`

```c
uint8_t bt_cts_time_format::mday
```

<a id="a299d6432d9b44b0de0be9c130733eb69"></a>

### `min`

```c
uint8_t bt_cts_time_format::min
```

<a id="a079a1c49698b6e9cb84291acdd1cf687"></a>

### `mon`

```c
uint8_t bt_cts_time_format::mon
```

<a id="a3482e00650e9e9a63816709c82a1aa07"></a>

### `reason`

```c
uint8_t bt_cts_time_format::reason
```

<a id="ae0ccd07b2a280888f3881f0d2fc2add6"></a>

### `sec`

```c
uint8_t bt_cts_time_format::sec
```

<a id="ae696cbbd3a785c1df6d54ce771f1d7a2"></a>

### `wday`

```c
uint8_t bt_cts_time_format::wday
```

<a id="ad5ab55fcb3e1dbaa73ba4ecb78d6b47e"></a>

### `year`

```c
uint16_t bt_cts_time_format::year
```

本数据类型文档由以下文件生成：

- `zephyr/bluetooth/services/cts.h`

## 65.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/services/cts.h](https://docs.zephyrproject.org/latest/doxygen/html/cts_8h_source.html)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P064_bt_cts_local_time_结构体.md) · [返回大纲](大纲.md) · [下一章](P066_bt_ets_cb_结构体.md)
