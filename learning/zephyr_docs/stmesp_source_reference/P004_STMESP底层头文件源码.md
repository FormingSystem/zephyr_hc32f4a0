---
id: learning.zephyr-docs.stmesp-source-reference.page-4
title: STMESP底层头文件源码
kind: reference
status: maintained
domains: [zephyr, kernel, source, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/stmesp_8h_source.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第4章\_STMESP底层头文件源码

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/stmesp_8h_source.html)。读取日期：2026-10-15；摘要见[来源记录](../SOURCES.md)。

本页保留官方Doxygen源码浏览页的全部可见代码及注释，移除展示行号、还原不换行空格并清除行尾空白。代码、标识符与许可证不翻译替换，中文对照列在后面。原网页隐藏了部分API文档注释，所以原始行号会跳跃；相关页面见[头文件参考](P003_STMESP底层头文件参考.md)和[公共接口](P003_STMESP底层头文件参考.md)；访问语义和生命周期见本页译注。

## 4.1\_原始可见代码（Source Code）

原始行号锚点保留在对应代码行，使用Markdown内嵌HTML预格式代码容器承载。

<a id="foldopen00099"></a>
<a id="foldopen00124"></a>
<a id="foldopen00138"></a>
<a id="foldopen00152"></a>
<a id="foldopen00169"></a>
<a id="adevicetree_8h_html"></a>
<a id="agroup__devicetree-generic-id_html_gab7d23294a6bf7fd44a98b48ec47d8a79"></a>
<a id="agroup__devicetree-reg-prop_html_gac6d8279c32351ced4c0ac7f32270974e"></a>
<a id="agroup__devicetree-reg-prop_html_gad223efc6c77d008e55c3588953e85bfb"></a>
<a id="agroup__stmsp__interface_html_ga2ffcc08b7d5c32c90b5d24982c0f6349"></a>
<a id="agroup__stmsp__interface_html_ga4350f5d201e3591221a932aa9fc3e94d"></a>
<a id="agroup__stmsp__interface_html_ga4af9486d77c93a55f221c7647d69a9f2"></a>
<a id="agroup__stmsp__interface_html_gaa7885c5a7620e46a532dbf405bfc6034"></a>
<a id="agroup__stmsp__interface_html_gaef1918a9d15d8da34fb5f2d7a11ff5fd"></a>
<a id="agroup__system__errno_html_ga2d1678d5a7cc8ce499643f3b8957def4"></a>
<a id="astdint_8h_html_a0a8582351ac627ee8bde2973c825e47f"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="astdint_8h_html_a5debae8b2a1ec20a6694c0c443ee399e"></a>

<pre><code class="language-c"><a id="l00001"></a>/*
<a id="l00002"></a> * Copyright (c) 2024 Nordic Semiconductor ASA
<a id="l00003"></a> *
<a id="l00004"></a> * SPDX-License-Identifier: Apache-2.0
<a id="l00005"></a> */
<a id="l00006"></a>
<a id="l00007"></a>#ifndef ZEPHYR_INCLUDE_DRIVERS_DEBUG_CORESIGHT_STMESP_H_
<a id="l00008"></a>#define ZEPHYR_INCLUDE_DRIVERS_DEBUG_CORESIGHT_STMESP_H_
<a id="l00009"></a>
<a id="l00010"></a>#include &lt;zephyr/devicetree.h&gt;
<a id="l00011"></a>
<a id="l00018"></a>
<a id="l00019"></a>#ifdef __cplusplus
<a id="l00020"></a>extern "C" {
<a id="l00021"></a>#endif
<a id="l00022"></a>
<a id="l00026"></a>typedef struct {
<a id="l00027"></a>        volatile uint32_t G_DMTS[2];
<a id="l00028"></a>        volatile uint32_t G_DM[2];
<a id="l00029"></a>        volatile uint32_t G_DTS[2];
<a id="l00030"></a>        volatile uint32_t G_D[2];
<a id="l00031"></a>        volatile uint32_t RESERVED0[16];
<a id="l00032"></a>        volatile uint32_t G_FLAGTS[2];
<a id="l00033"></a>        volatile uint32_t G_FLAG[2];
<a id="l00034"></a>        volatile uint32_t G_TRIGTS[2];
<a id="l00035"></a>        volatile uint32_t G_TRIG[2];
<a id="l00036"></a>        volatile uint32_t I_DMTS[2];
<a id="l00037"></a>        volatile uint32_t I_DM[2];
<a id="l00038"></a>        volatile uint32_t I_DTS[2];
<a id="l00039"></a>        volatile uint32_t I_D[2];
<a id="l00040"></a>        volatile uint32_t RESERVED1[16];
<a id="l00041"></a>        volatile uint32_t I_FLAGTS[2];
<a id="l00042"></a>        volatile uint32_t I_FLAG[2];
<a id="l00043"></a>        volatile uint32_t I_TRIGTS[2];
<a id="l00044"></a>        volatile uint32_t I_TRIG[2];
<a id="l00045"></a>} STMESP_Type;
<a id="l00046"></a>
<a id="l00056"></a>static inline volatile void *_stmesp_get_data_reg(STMESP_Type *reg, bool ts,
<a id="l00057"></a>                                                  bool marked, bool guaranteed)
<a id="l00058"></a>{
<a id="l00059"></a>        if (ts) {
<a id="l00060"></a>                if (guaranteed) {
<a id="l00061"></a>                        if (marked) {
<a id="l00062"></a>                                return &amp;reg-&gt;G_DMTS[0];
<a id="l00063"></a>                        } else {
<a id="l00064"></a>                                return &amp;reg-&gt;G_DTS[0];
<a id="l00065"></a>                        }
<a id="l00066"></a>                } else {
<a id="l00067"></a>                        if (marked) {
<a id="l00068"></a>                                return &amp;reg-&gt;I_DMTS[0];
<a id="l00069"></a>                        } else {
<a id="l00070"></a>                                return &amp;reg-&gt;I_DTS[0];
<a id="l00071"></a>                        }
<a id="l00072"></a>                }
<a id="l00073"></a>        } else {
<a id="l00074"></a>                if (guaranteed) {
<a id="l00075"></a>                        if (marked) {
<a id="l00076"></a>                                return &amp;reg-&gt;G_DM[0];
<a id="l00077"></a>                        } else {
<a id="l00078"></a>                                return &amp;reg-&gt;G_D[0];
<a id="l00079"></a>                        }
<a id="l00080"></a>                } else {
<a id="l00081"></a>                        if (marked) {
<a id="l00082"></a>                                return &amp;reg-&gt;I_DM[0];
<a id="l00083"></a>                        } else {
<a id="l00084"></a>                                return &amp;reg-&gt;I_D[0];
<a id="l00085"></a>                        }
<a id="l00086"></a>                }
<a id="l00087"></a>        }
<a id="l00088"></a>}
<a id="l00089"></a>
<a id="l00091"></a>
<a id="l00099"></a>static inline void stmesp_flag(STMESP_Type *reg, uint32_t data, bool ts, bool guaranteed)
<a id="l00100"></a>{
<a id="l00101"></a>        if (ts) {
<a id="l00102"></a>                if (guaranteed) {
<a id="l00103"></a>                        reg-&gt;G_FLAGTS[0] = data;
<a id="l00104"></a>                } else {
<a id="l00105"></a>                        reg-&gt;I_FLAGTS[0] = data;
<a id="l00106"></a>                }
<a id="l00107"></a>        } else {
<a id="l00108"></a>                if (guaranteed) {
<a id="l00109"></a>                        reg-&gt;G_FLAG[0] = data;
<a id="l00110"></a>                } else {
<a id="l00111"></a>                        reg-&gt;I_FLAG[0] = data;
<a id="l00112"></a>                }
<a id="l00113"></a>        }
<a id="l00114"></a>}
<a id="l00115"></a>
<a id="l00124"></a>static inline void stmesp_data8(STMESP_Type *reg, uint8_t data, bool ts,
<a id="l00125"></a>                                bool marked, bool guaranteed)
<a id="l00126"></a>{
<a id="l00127"></a>        *(volatile uint8_t *)_stmesp_get_data_reg(reg, ts, marked, guaranteed) = data;
<a id="l00128"></a>}
<a id="l00129"></a>
<a id="l00138"></a>static inline void stmesp_data16(STMESP_Type *reg, uint16_t data, bool ts,
<a id="l00139"></a>                                 bool marked, bool guaranteed)
<a id="l00140"></a>{
<a id="l00141"></a>        *(volatile uint16_t *)_stmesp_get_data_reg(reg, ts, marked, guaranteed) = data;
<a id="l00142"></a>}
<a id="l00143"></a>
<a id="l00152"></a>static inline void stmesp_data32(STMESP_Type *reg, uint32_t data, bool ts,
<a id="l00153"></a>                                 bool marked, bool guaranteed)
<a id="l00154"></a>{
<a id="l00155"></a>        *(volatile uint32_t *)_stmesp_get_data_reg(reg, ts, marked, guaranteed) = data;
<a id="l00156"></a>}
<a id="l00157"></a>
<a id="l00169"></a>static inline int stmesp_get_port(uint32_t idx, STMESP_Type **port)
<a id="l00170"></a>
<a id="l00171"></a>{
<a id="l00172"></a>        /* Check if index is within STM ports */
<a id="l00173"></a>        if ((port == NULL) ||
<a id="l00174"></a>            (idx &gt;= (DT_REG_SIZE(DT_NODELABEL(stmesp)) / sizeof(STMESP_Type)))) {
<a id="l00175"></a>                return -EINVAL;
<a id="l00176"></a>        }
<a id="l00177"></a>
<a id="l00178"></a>        STMESP_Type *const base = (STMESP_Type *const)DT_REG_ADDR(DT_NODELABEL(stmesp));
<a id="l00179"></a>
<a id="l00180"></a>        *port = &amp;base[idx];
<a id="l00181"></a>
<a id="l00182"></a>        return 0;
<a id="l00183"></a>}
<a id="l00184"></a>
<a id="l00185"></a>#ifdef __cplusplus
<a id="l00186"></a>}
<a id="l00187"></a>#endif
<a id="l00188"></a>
<a id="l00192"></a>
<a id="l00193"></a>#endif /* ZEPHYR_INCLUDE_DRIVERS_DEBUG_CORESIGHT_STMESP_H_ */
</code></pre>

## 4.2\_可见注释译文（Comments）

1. 版权与许可证：Copyright (c) 2024 Nordic Semiconductor ASA；SPDX-License-Identifier: Apache-2.0。原始法律声明保留。

2. 检查索引是否位于STM端口范围内。

3. ZEPHYR_INCLUDE_DRIVERS_DEBUG_CORESIGHT_STMESP_H_头文件包含保护结束。

## 4.3\_原页符号提示（Symbol Descriptions）

### `devicetree.h`

设备树（Devicetree）主头文件。

符号定位：[devicetree.h](../dt_main_reference/P001_设备树主头文件参考.md)。

### `DT_NODELABEL`

```c
#define DT_NODELABEL(label)
```

根据节点标签（Node Label）取得节点标识符（Node Identifier）。

定义位置（Definition）：devicetree.h:197。

符号定位：[DT_NODELABEL](../dt_identity_reference/P001_设备树节点标识宏.md#gab7d23294a6bf7fd44a98b48ec47d8a79)。

### `DT_REG_ADDR`

```c
#define DT_REG_ADDR(node_id)
```

取得节点唯一寄存器块（Register Block）的地址。

定义位置（Definition）：devicetree.h:2881。

符号定位：[DT_REG_ADDR](../dt_reg_reference/P001_设备树寄存器属性宏.md#gac6d8279c32351ced4c0ac7f32270974e)。

### `DT_REG_SIZE`

```c
#define DT_REG_SIZE(node_id)
```

取得节点唯一寄存器块（Register Block）的大小。

定义位置（Definition）：devicetree.h:2902。

符号定位：[DT_REG_SIZE](../dt_reg_reference/P001_设备树寄存器属性宏.md#gad223efc6c77d008e55c3588953e85bfb)。

### `stmesp_flag`

```c
static void stmesp_flag(STMESP_Type *reg, uint32_t data, bool ts, bool guaranteed)
```

向STMESP写入标志（Flag）。

定义位置（Definition）：stmesp.h:99。

符号定位：[stmesp_flag](../trace_interface_reference/P002_STMESP底层接口.md#ga2ffcc08b7d5c32c90b5d24982c0f6349)。

### `stmesp_get_port`

```c
static int stmesp_get_port(uint32_t idx, STMESP_Type **port)
```

返回系统跟踪宏单元扩展激励端口（STM Extended Stimulus Port）的地址。

定义位置（Definition）：stmesp.h:169。

符号定位：[stmesp_get_port](../trace_interface_reference/P002_STMESP底层接口.md#ga4350f5d201e3591221a932aa9fc3e94d)。

### `stmesp_data8`

```c
static void stmesp_data8(STMESP_Type *reg, uint8_t data, bool ts, bool marked, bool guaranteed)
```

向STMESP写入8位数据（8-bit Data）。

定义位置（Definition）：stmesp.h:124。

符号定位：[stmesp_data8](../trace_interface_reference/P002_STMESP底层接口.md#ga4af9486d77c93a55f221c7647d69a9f2)。

### `stmesp_data32`

```c
static void stmesp_data32(STMESP_Type *reg, uint32_t data, bool ts, bool marked, bool guaranteed)
```

向STMESP写入32位数据（32-bit Data）。

定义位置（Definition）：stmesp.h:152。

符号定位：[stmesp_data32](../trace_interface_reference/P002_STMESP底层接口.md#gaa7885c5a7620e46a532dbf405bfc6034)。

### `stmesp_data16`

```c
static void stmesp_data16(STMESP_Type *reg, uint16_t data, bool ts, bool marked, bool guaranteed)
```

向STMESP写入16位数据（16-bit Data）。

定义位置（Definition）：stmesp.h:138。

符号定位：[stmesp_data16](../trace_interface_reference/P002_STMESP底层接口.md#gaef1918a9d15d8da34fb5f2d7a11ff5fd)。

### `EINVAL`

```c
#define EINVAL
```

参数无效（Invalid Argument）。

定义位置（Definition）：errno.h:61。

符号定位：[EINVAL](../error_reference/P003_系统错误号公共接口.md#ga2d1678d5a7cc8ce499643f3b8957def4)。

### `uint32_t`

```c
__UINT32_TYPE__ uint32_t
```

定义位置（Definition）：stdint.h:90。

符号定位：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)。

### `uint8_t`

```c
__UINT8_TYPE__ uint8_t
```

定义位置（Definition）：stdint.h:88。

符号定位：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

### `uint16_t`

```c
__UINT16_TYPE__ uint16_t
```

定义位置（Definition）：stdint.h:89。

符号定位：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)。

## 4.4\_源码跟踪译注

> 译注——系统跟踪宏单元（System Trace Macrocell，STM）的扩展激励端口（Extended Stimulus Port，ESP）采用内存映射寄存器访问（MMIO）。data8、data16、data32分别通过volatile指针执行对应位宽的写入，不是向普通RAM缓冲区复制日志。

> 译注——时间戳（Timestamp）、标记（Marked）和保证型访问（Guaranteed Access）决定选用哪组寄存器。Guaranteed指STM访问类别，不能据此推断主机最终收到并解码了每条日志。

> 译注——stmesp_get_port先检查输出指针是否为NULL，以及idx是否小于设备树寄存器区域大小除以单个STMESP_Type的大小。成功才写出端口地址；失败返回-EINVAL且不改写输出。idx是端口索引，不是字节地址。

> 译注——取得端口地址依赖设备树（Devicetree）中stmesp节点的地址和大小，并不完成跟踪硬件、嵌入式跟踪路由器（Embedded Trace Router，ETR）或主机解码工具的初始化。

头文件定位：[include/zephyr/drivers/debug/stmesp.h](../../../include/zephyr/drivers/debug/stmesp.h)，关联实现／接口：[include/zephyr/drivers/debug/stmesp.h](../../../include/zephyr/drivers/debug/stmesp.h)；[官方原始头文件](https://github.com/zephyrproject-rtos/zephyr/blob/main/include/zephyr/drivers/debug/stmesp.h)与[官方关联文件](https://github.com/zephyrproject-rtos/zephyr/blob/main/include/zephyr/drivers/debug/stmesp.h)的摘要见来源记录。去掉注释和展示空白后，本页代码与本次读取的原始头文件一致，不能推广到以后滚动更新的main或任意本地版本。

本次验证范围为文档与源码对照，未构建固件、配置实板引脚或操作硬件。

## 4.5\_原页交叉引用（Cross References）

- [查看此文件参考说明](P003_STMESP底层头文件参考.md)
- [zephyr/devicetree.h](../dt_main_reference/P001_设备树主头文件参考.md)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [stmesp_flag](../trace_interface_reference/P002_STMESP底层接口.md#ga2ffcc08b7d5c32c90b5d24982c0f6349)
- [stmesp_data8](../trace_interface_reference/P002_STMESP底层接口.md#ga4af9486d77c93a55f221c7647d69a9f2)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [stmesp_data16](../trace_interface_reference/P002_STMESP底层接口.md#gaef1918a9d15d8da34fb5f2d7a11ff5fd)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [stmesp_data32](../trace_interface_reference/P002_STMESP底层接口.md#gaa7885c5a7620e46a532dbf405bfc6034)
- [stmesp_get_port](../trace_interface_reference/P002_STMESP底层接口.md#ga4350f5d201e3591221a932aa9fc3e94d)
- [DT_REG_SIZE](../dt_reg_reference/P001_设备树寄存器属性宏.md#gad223efc6c77d008e55c3588953e85bfb)
- [DT_NODELABEL](../dt_identity_reference/P001_设备树节点标识宏.md#gab7d23294a6bf7fd44a98b48ec47d8a79)
- [EINVAL](../error_reference/P003_系统错误号公共接口.md#ga2d1678d5a7cc8ce499643f3b8957def4)
- [DT_REG_ADDR](../dt_reg_reference/P001_设备树寄存器属性宏.md#gac6d8279c32351ced4c0ac7f32270974e)

---

[上一章](P003_STMESP底层头文件参考.md) · [返回大纲](大纲.md)
