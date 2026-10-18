---
id: learning.zephyr-docs.api-file-reference.page-69
title: zephyr__dt-bindings__pcie__pcie.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/dt-bindings_2pcie_2pcie_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第69章\_zephyr\_\_dt-bindings\_\_pcie\_\_pcie.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/dt-bindings_2pcie_2pcie_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

查看此文件的源码。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 69.1\_宏定义（Macros）

<a id="r_af0887b3d40d4ea7e2c45b750428c7268"></a>

```c
#define PCIE_IRQ_DETECT 0xFFFFFFFU
```

相关声明：[PCIE_IRQ_DETECT](#af0887b3d40d4ea7e2c45b750428c7268)。

<a id="r_a1c7936d783359e8fa84236dfa852c701"></a>

```c
#define PCIE_ID_VEND_SHIFT 0U
```

相关声明：[PCIE_ID_VEND_SHIFT](#a1c7936d783359e8fa84236dfa852c701)。

<a id="r_a4d9c60447a305f7f969f0f49d04afba6"></a>

```c
#define PCIE_ID_VEND_MASK 0xFFFFU
```

相关声明：[PCIE_ID_VEND_MASK](#a4d9c60447a305f7f969f0f49d04afba6)。

<a id="r_ab6c544956c1bdc670bd3ce8f541b8807"></a>

```c
#define PCIE_ID_DEV_SHIFT 16U
```

相关声明：[PCIE_ID_DEV_SHIFT](#ab6c544956c1bdc670bd3ce8f541b8807)。

<a id="r_a6ebb481752bacbea6d7b3febb4a8ad5c"></a>

```c
#define PCIE_ID_DEV_MASK 0xFFFFU
```

相关声明：[PCIE_ID_DEV_MASK](#a6ebb481752bacbea6d7b3febb4a8ad5c)。

<a id="r_a5cc7a8d3810218cc9582df360ad58cb8"></a>

```c
#define CAST(type, v)
```

相关声明：[CAST](#a5cc7a8d3810218cc9582df360ad58cb8)。

<a id="r_af3107df4821c35c5f217a2b8bc49bce6"></a>

```c
#define PCIE_ID(vend, dev)
```

相关声明：[PCIE_ID](#af3107df4821c35c5f217a2b8bc49bce6)。

<a id="r_aa99534d1e5bfed4e1a57d8534a534045"></a>

```c
#define PCIE_ID_TO_VEND(id)
```

相关声明：[PCIE_ID_TO_VEND](#aa99534d1e5bfed4e1a57d8534a534045)。

<a id="r_aa2198fcdc69f0d86d120355342781a62"></a>

```c
#define PCIE_ID_TO_DEV(id)
```

相关声明：[PCIE_ID_TO_DEV](#aa2198fcdc69f0d86d120355342781a62)。

<a id="r_a23ce79d01609cb14f0cd4b2298e13b14"></a>

```c
#define PCIE_ID_NONE PCIE_ID(0xFFFF, 0xFFFF)
```

相关声明：[PCIE_ID_NONE](#a23ce79d01609cb14f0cd4b2298e13b14)、[PCIE_ID](#af3107df4821c35c5f217a2b8bc49bce6)。

<a id="r_a6268e6c107a85fbc6035eca5e6b3cfd6"></a>

```c
#define PCIE_BDF_NONE 0xFFFFFFFFU
```

相关声明：[PCIE_BDF_NONE](#a6268e6c107a85fbc6035eca5e6b3cfd6)。

<a id="r_ada4a5da3eabff1240e651b18e8b10ca7"></a>

```c
#define PCIE_BDF_BUS_SHIFT 16U
```

相关声明：[PCIE_BDF_BUS_SHIFT](#ada4a5da3eabff1240e651b18e8b10ca7)。

<a id="r_a193dd359d7a96bdd904662717c7fbf6d"></a>

```c
#define PCIE_BDF_BUS_MASK 0xFFU
```

相关声明：[PCIE_BDF_BUS_MASK](#a193dd359d7a96bdd904662717c7fbf6d)。

<a id="r_a7b6be889b801a52f7a713cbf7f2924f6"></a>

```c
#define PCIE_BDF_DEV_SHIFT 11U
```

相关声明：[PCIE_BDF_DEV_SHIFT](#a7b6be889b801a52f7a713cbf7f2924f6)。

<a id="r_a85cc69963a93046bda0f1594803af9eb"></a>

```c
#define PCIE_BDF_DEV_MASK 0x1FU
```

相关声明：[PCIE_BDF_DEV_MASK](#a85cc69963a93046bda0f1594803af9eb)。

<a id="r_aa14155ded76c4587c49d0a71e25166cc"></a>

```c
#define PCIE_BDF_FUNC_SHIFT 8U
```

相关声明：[PCIE_BDF_FUNC_SHIFT](#aa14155ded76c4587c49d0a71e25166cc)。

<a id="r_ab481360fa29cf086cc5369e6f1860a5f"></a>

```c
#define PCIE_BDF_FUNC_MASK 0x7U
```

相关声明：[PCIE_BDF_FUNC_MASK](#ab481360fa29cf086cc5369e6f1860a5f)。

<a id="r_a09a440a45623a282c23eaa2cfeef63d2"></a>

```c
#define PCIE_BDF(bus, dev, func)
```

相关声明：[PCIE_BDF](#a09a440a45623a282c23eaa2cfeef63d2)。

<a id="r_a1c5051a72c50d6ee6cb72cd8d5c41a16"></a>

```c
#define PCIE_BDF_TO_BUS(bdf)
```

相关声明：[PCIE_BDF_TO_BUS](#a1c5051a72c50d6ee6cb72cd8d5c41a16)。

<a id="r_ad97fbff75fe4aa3bacad0f952e7349e9"></a>

```c
#define PCIE_BDF_TO_DEV(bdf)
```

相关声明：[PCIE_BDF_TO_DEV](#ad97fbff75fe4aa3bacad0f952e7349e9)。

<a id="r_ab5faa8800faa83015623439447dc0fe7"></a>

```c
#define PCIE_BDF_TO_FUNC(bdf)
```

相关声明：[PCIE_BDF_TO_FUNC](#ab5faa8800faa83015623439447dc0fe7)。

## 69.2\_详细说明（Detailed Documentation）

<a id="a5cc7a8d3810218cc9582df360ad58cb8"></a>

### `CAST`

```c
#define CAST ( type, v )
```

展开值（Value）：

```c
((type)(v))
```

<a id="a09a440a45623a282c23eaa2cfeef63d2"></a>

### `PCIE_BDF`

```c
#define PCIE_BDF ( bus, dev, func )
```

展开值（Value）：

```c
((((bus) & PCIE_BDF_BUS_MASK) << PCIE_BDF_BUS_SHIFT) | \
 (((dev) & PCIE_BDF_DEV_MASK) << PCIE_BDF_DEV_SHIFT) | \
 (((func) & PCIE_BDF_FUNC_MASK) << PCIE_BDF_FUNC_SHIFT))
```

<a id="a193dd359d7a96bdd904662717c7fbf6d"></a>

### `PCIE_BDF_BUS_MASK`

```c
#define PCIE_BDF_BUS_MASK 0xFFU
```

<a id="ada4a5da3eabff1240e651b18e8b10ca7"></a>

### `PCIE_BDF_BUS_SHIFT`

```c
#define PCIE_BDF_BUS_SHIFT 16U
```

<a id="a85cc69963a93046bda0f1594803af9eb"></a>

### `PCIE_BDF_DEV_MASK`

```c
#define PCIE_BDF_DEV_MASK 0x1FU
```

<a id="a7b6be889b801a52f7a713cbf7f2924f6"></a>

### `PCIE_BDF_DEV_SHIFT`

```c
#define PCIE_BDF_DEV_SHIFT 11U
```

<a id="ab481360fa29cf086cc5369e6f1860a5f"></a>

### `PCIE_BDF_FUNC_MASK`

```c
#define PCIE_BDF_FUNC_MASK 0x7U
```

<a id="aa14155ded76c4587c49d0a71e25166cc"></a>

### `PCIE_BDF_FUNC_SHIFT`

```c
#define PCIE_BDF_FUNC_SHIFT 8U
```

<a id="a6268e6c107a85fbc6035eca5e6b3cfd6"></a>

### `PCIE_BDF_NONE`

```c
#define PCIE_BDF_NONE 0xFFFFFFFFU
```

<a id="a1c5051a72c50d6ee6cb72cd8d5c41a16"></a>

### `PCIE_BDF_TO_BUS`

```c
#define PCIE_BDF_TO_BUS ( bdf)
```

展开值（Value）：

```c
(((bdf) >> PCIE_BDF_BUS_SHIFT) & PCIE_BDF_BUS_MASK)
```

<a id="ad97fbff75fe4aa3bacad0f952e7349e9"></a>

### `PCIE_BDF_TO_DEV`

```c
#define PCIE_BDF_TO_DEV ( bdf)
```

展开值（Value）：

```c
(((bdf) >> PCIE_BDF_DEV_SHIFT) & PCIE_BDF_DEV_MASK)
```

<a id="ab5faa8800faa83015623439447dc0fe7"></a>

### `PCIE_BDF_TO_FUNC`

```c
#define PCIE_BDF_TO_FUNC ( bdf)
```

展开值（Value）：

```c
(((bdf) >> PCIE_BDF_FUNC_SHIFT) & PCIE_BDF_FUNC_MASK)
```

<a id="af3107df4821c35c5f217a2b8bc49bce6"></a>

### `PCIE_ID`

```c
#define PCIE_ID ( vend, dev )
```

展开值（Value）：

```c
((((vend) & PCIE_ID_VEND_MASK) << PCIE_ID_VEND_SHIFT) | \
 (CAST(uint32_t, (dev) & PCIE_ID_DEV_MASK) << PCIE_ID_DEV_SHIFT))
```

<a id="a6ebb481752bacbea6d7b3febb4a8ad5c"></a>

### `PCIE_ID_DEV_MASK`

```c
#define PCIE_ID_DEV_MASK 0xFFFFU
```

<a id="ab6c544956c1bdc670bd3ce8f541b8807"></a>

### `PCIE_ID_DEV_SHIFT`

```c
#define PCIE_ID_DEV_SHIFT 16U
```

<a id="a23ce79d01609cb14f0cd4b2298e13b14"></a>

### `PCIE_ID_NONE`

```c
#define PCIE_ID_NONE PCIE_ID(0xFFFF, 0xFFFF)
```

<a id="aa2198fcdc69f0d86d120355342781a62"></a>

### `PCIE_ID_TO_DEV`

```c
#define PCIE_ID_TO_DEV ( id)
```

展开值（Value）：

```c
(((id) >> PCIE_ID_DEV_SHIFT) & PCIE_ID_DEV_MASK)
```

<a id="aa99534d1e5bfed4e1a57d8534a534045"></a>

### `PCIE_ID_TO_VEND`

```c
#define PCIE_ID_TO_VEND ( id)
```

展开值（Value）：

```c
(((id) >> PCIE_ID_VEND_SHIFT) & PCIE_ID_VEND_MASK)
```

<a id="a4d9c60447a305f7f969f0f49d04afba6"></a>

### `PCIE_ID_VEND_MASK`

```c
#define PCIE_ID_VEND_MASK 0xFFFFU
```

<a id="a1c7936d783359e8fa84236dfa852c701"></a>

### `PCIE_ID_VEND_SHIFT`

```c
#define PCIE_ID_VEND_SHIFT 0U
```

<a id="af0887b3d40d4ea7e2c45b750428c7268"></a>

### `PCIE_IRQ_DETECT`

```c
#define PCIE_IRQ_DETECT 0xFFFFFFFU
```


## 69.3\_原页交叉引用（Cross References）

- [查看此文件的源码。](../api_source_runtime_reference/P016_pcie.h_源码浏览.md)
- [uint32_t](P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)

<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="adt-bindings_2pcie_2pcie_8h_html_a193dd359d7a96bdd904662717c7fbf6d"></a>
<a id="adt-bindings_2pcie_2pcie_8h_html_a7b6be889b801a52f7a713cbf7f2924f6"></a>
<a id="adt-bindings_2pcie_2pcie_8h_html_a85cc69963a93046bda0f1594803af9eb"></a>
<a id="adt-bindings_2pcie_2pcie_8h_html_aa14155ded76c4587c49d0a71e25166cc"></a>
<a id="adt-bindings_2pcie_2pcie_8h_html_ab481360fa29cf086cc5369e6f1860a5f"></a>
<a id="adt-bindings_2pcie_2pcie_8h_html_ada4a5da3eabff1240e651b18e8b10ca7"></a>
<a id="adt-bindings_2pcie_2pcie_8h_html_a1c7936d783359e8fa84236dfa852c701"></a>
<a id="adt-bindings_2pcie_2pcie_8h_html_a4d9c60447a305f7f969f0f49d04afba6"></a>
<a id="adt-bindings_2pcie_2pcie_8h_html_a5cc7a8d3810218cc9582df360ad58cb8"></a>
<a id="adt-bindings_2pcie_2pcie_8h_html_a6ebb481752bacbea6d7b3febb4a8ad5c"></a>
<a id="adt-bindings_2pcie_2pcie_8h_html_ab6c544956c1bdc670bd3ce8f541b8807"></a>
<a id="astdint_8h_html_a0a8582351ac627ee8bde2973c825e47f"></a>

---

[上一章](P068_zephyr__dt-bindings__misc__nxp_rtxxx_dsp_ctrl.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P070_zephyr__dt-bindings__power__atmel_sam_supc.h_文件参考.md)
