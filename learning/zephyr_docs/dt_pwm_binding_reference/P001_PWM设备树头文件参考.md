---
id: learning.zephyr-docs.dt-pwm-binding-reference.page-1
title: PWM设备树头文件参考
kind: reference
status: maintained
domains: [zephyr, hardware, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/pwms_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第1章\_PWM设备树头文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/pwms_8h.html)。读取日期：2026-10-15；来源摘要见[来源记录](../SOURCES.md)。

> 译注——阅读位置：从[本册大纲](大纲.md)选择PWM设备树访问或PWM、I2C绑定常量头文件，再通过接口链接进入完整说明。源码跟踪译注与官方原文分开标示。

PWM（脉宽调制，Pulse Width Modulation）设备树宏公共 API 头文件。

查看此文件的源码。

<a id="details"></a>

PWM（脉宽调制，Pulse Width Modulation）设备树宏公共 API 头文件。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 1.1\_宏定义（Macros）

<a id="r_ga2f16d00a53717a66668fb8bc967acce5"></a>

```c
#define DT_PWMS_CTLR_BY_IDX(node_id, idx)
```

相关声明：[DT_PWMS_CTLR_BY_IDX](../hardware/P264_设备树PWM宏.md#ga2f16d00a53717a66668fb8bc967acce5)。

按索引从 `pwms` 属性取得 PWM 控制器的节点标识符（Node Identifier）。

<a id="r_ga6922e69c707219cd766fe317484dac8a"></a>

```c
#define DT_PWMS_CTLR_BY_NAME(node_id, name)
```

相关声明：[DT_PWMS_CTLR_BY_NAME](../hardware/P264_设备树PWM宏.md#ga6922e69c707219cd766fe317484dac8a)。

按名称从 `pwms` 属性取得 PWM 控制器的节点标识符。

<a id="r_gaff7a0b201d97a1d1bb1893b556d5a194"></a>

```c
#define DT_PWMS_CTLR(node_id)
```

相关声明：[DT_PWMS_CTLR](../hardware/P264_设备树PWM宏.md#gaff7a0b201d97a1d1bb1893b556d5a194)。

等价于 `DT_PWMS_CTLR_BY_IDX(node_id, 0)`。

<a id="r_ga0c1ab3329448f92936d57a83b5b3594e"></a>

```c
#define DT_PWMS_CELL_BY_IDX(node_id, idx, cell)
```

相关声明：[DT_PWMS_CELL_BY_IDX](../hardware/P264_设备树PWM宏.md#ga0c1ab3329448f92936d57a83b5b3594e)。

按索引取得 PWM 说明符（PWM Specifier）的参数单元（Cell）值。

<a id="r_ga69233198a489283068bc1ded5072ca26"></a>

```c
#define DT_PWMS_CELL_BY_NAME(node_id, name, cell)
```

相关声明：[DT_PWMS_CELL_BY_NAME](../hardware/P264_设备树PWM宏.md#ga69233198a489283068bc1ded5072ca26)。

按名称取得 PWM 说明符的参数单元值。

<a id="r_ga2062b31a090c05ccd267ae1468b182ef"></a>

```c
#define DT_PWMS_CELL(node_id, cell)
```

相关声明：[DT_PWMS_CELL](../hardware/P264_设备树PWM宏.md#ga2062b31a090c05ccd267ae1468b182ef)。

等价于 `DT_PWMS_CELL_BY_IDX(node_id, 0, cell)`。

<a id="r_ga10a372e44c7e3feb551ca996c6ca5a8f"></a>

```c
#define DT_PWMS_CHANNEL_BY_IDX(node_id, idx)
```

相关声明：[DT_PWMS_CHANNEL_BY_IDX](../hardware/P264_设备树PWM宏.md#ga10a372e44c7e3feb551ca996c6ca5a8f)。

按索引取得 PWM 说明符的 `channel` 参数单元值。

<a id="r_ga59a4b9884e9620eac04c3808a3a6d164"></a>

```c
#define DT_PWMS_CHANNEL_BY_NAME(node_id, name)
```

相关声明：[DT_PWMS_CHANNEL_BY_NAME](../hardware/P264_设备树PWM宏.md#ga59a4b9884e9620eac04c3808a3a6d164)。

按名称取得 PWM 说明符的 `channel` 参数单元值。

<a id="r_gaeb0a10ad37fdfd3dcc75bd379908acdc"></a>

```c
#define DT_PWMS_CHANNEL(node_id)
```

相关声明：[DT_PWMS_CHANNEL](../hardware/P264_设备树PWM宏.md#gaeb0a10ad37fdfd3dcc75bd379908acdc)。

等价于 `DT_PWMS_CHANNEL_BY_IDX(node_id, 0)`。

<a id="r_ga9456f65777e6fc7c057c6e0709c9245f"></a>

```c
#define DT_PWMS_PERIOD_BY_IDX(node_id, idx)
```

相关声明：[DT_PWMS_PERIOD_BY_IDX](../hardware/P264_设备树PWM宏.md#ga9456f65777e6fc7c057c6e0709c9245f)。

按索引取得 PWM 说明符的 `period` 参数单元值。

<a id="r_ga74af83d31fc38f331808dedfaecf4c74"></a>

```c
#define DT_PWMS_PERIOD_BY_NAME(node_id, name)
```

相关声明：[DT_PWMS_PERIOD_BY_NAME](../hardware/P264_设备树PWM宏.md#ga74af83d31fc38f331808dedfaecf4c74)。

按名称取得 PWM 说明符的 `period` 参数单元值。

<a id="r_gac6006a723932325b96a1b50619be153b"></a>

```c
#define DT_PWMS_PERIOD(node_id)
```

相关声明：[DT_PWMS_PERIOD](../hardware/P264_设备树PWM宏.md#gac6006a723932325b96a1b50619be153b)。

等价于 `DT_PWMS_PERIOD_BY_IDX(node_id, 0)`。

<a id="r_gaf9c1ac7f3a39f4022f3ec31ef8de98e6"></a>

```c
#define DT_PWMS_FLAGS_BY_IDX(node_id, idx)
```

相关声明：[DT_PWMS_FLAGS_BY_IDX](../hardware/P264_设备树PWM宏.md#gaf9c1ac7f3a39f4022f3ec31ef8de98e6)。

按索引取得 PWM 说明符的 `flags` 参数单元值。

<a id="r_ga7a1621bfb223da23aa030b64fc0c0bcd"></a>

```c
#define DT_PWMS_FLAGS_BY_NAME(node_id, name)
```

相关声明：[DT_PWMS_FLAGS_BY_NAME](../hardware/P264_设备树PWM宏.md#ga7a1621bfb223da23aa030b64fc0c0bcd)。

按名称取得 PWM 说明符的 `flags` 参数单元值。

<a id="r_ga8dcd2d18129504d1a4ab71ae05c48c44"></a>

```c
#define DT_PWMS_FLAGS(node_id)
```

相关声明：[DT_PWMS_FLAGS](../hardware/P264_设备树PWM宏.md#ga8dcd2d18129504d1a4ab71ae05c48c44)。

等价于 `DT_PWMS_FLAGS_BY_IDX(node_id, 0)`。

<a id="r_ga4f751ba5f3c1aad5d62178b166f36c24"></a>

```c
#define DT_INST_PWMS_CTLR_BY_IDX(inst, idx)
```

相关声明：[DT_INST_PWMS_CTLR_BY_IDX](../hardware/P264_设备树PWM宏.md#ga4f751ba5f3c1aad5d62178b166f36c24)。

按索引从 `DT_DRV_COMPAT` 对应实例的 `pwms` 属性取得 PWM 控制器节点标识符。

<a id="r_gae66d3e710496bff9789996ddb72e1ebe"></a>

```c
#define DT_INST_PWMS_CTLR_BY_NAME(inst, name)
```

相关声明：[DT_INST_PWMS_CTLR_BY_NAME](../hardware/P264_设备树PWM宏.md#gae66d3e710496bff9789996ddb72e1ebe)。

按名称从 `DT_DRV_COMPAT` 对应实例的 `pwms` 属性取得 PWM 控制器节点标识符。

<a id="r_ga2f79a0a48e08c89bac58d16d9731e683"></a>

```c
#define DT_INST_PWMS_CTLR(inst)
```

相关声明：[DT_INST_PWMS_CTLR](../hardware/P264_设备树PWM宏.md#ga2f79a0a48e08c89bac58d16d9731e683)。

等价于 `DT_INST_PWMS_CTLR_BY_IDX(inst, 0)`。

<a id="r_gad106bf22d9dc90384519cd6ccc8fd1c6"></a>

```c
#define DT_INST_PWMS_CELL_BY_IDX(inst, idx, cell)
```

相关声明：[DT_INST_PWMS_CELL_BY_IDX](../hardware/P264_设备树PWM宏.md#gad106bf22d9dc90384519cd6ccc8fd1c6)。

按索引取得 `DT_DRV_COMPAT` 对应实例的 PWM 说明符参数单元值。

<a id="r_ga5731d949be09461f5da040e451cc509c"></a>

```c
#define DT_INST_PWMS_CELL_BY_NAME(inst, name, cell)
```

相关声明：[DT_INST_PWMS_CELL_BY_NAME](../hardware/P264_设备树PWM宏.md#ga5731d949be09461f5da040e451cc509c)。

按名称取得 `DT_DRV_COMPAT` 对应实例的 PWM 说明符参数单元值。

<a id="r_ga199804a2d06c301f19c5c8de232ede15"></a>

```c
#define DT_INST_PWMS_CELL(inst, cell)
```

相关声明：[DT_INST_PWMS_CELL](../hardware/P264_设备树PWM宏.md#ga199804a2d06c301f19c5c8de232ede15)。

等价于 `DT_INST_PWMS_CELL_BY_IDX(inst, 0, cell)`。

<a id="r_ga154ece84d782a7df2ce31b2a34f43870"></a>

```c
#define DT_INST_PWMS_CHANNEL_BY_IDX(inst, idx)
```

相关声明：[DT_INST_PWMS_CHANNEL_BY_IDX](../hardware/P264_设备树PWM宏.md#ga154ece84d782a7df2ce31b2a34f43870)。

等价于 `DT_INST_PWMS_CELL_BY_IDX(inst, idx, channel)`。

<a id="r_ga60901952d81e29dbfbbe88ee3ffe3e17"></a>

```c
#define DT_INST_PWMS_CHANNEL_BY_NAME(inst, name)
```

相关声明：[DT_INST_PWMS_CHANNEL_BY_NAME](../hardware/P264_设备树PWM宏.md#ga60901952d81e29dbfbbe88ee3ffe3e17)。

等价于 `DT_INST_PWMS_CELL_BY_NAME(inst, name, channel)`。

<a id="r_gad871b89fd1b2d62aae84dc35a0819032"></a>

```c
#define DT_INST_PWMS_CHANNEL(inst)
```

相关声明：[DT_INST_PWMS_CHANNEL](../hardware/P264_设备树PWM宏.md#gad871b89fd1b2d62aae84dc35a0819032)。

等价于 `DT_INST_PWMS_CHANNEL_BY_IDX(inst, 0)`。

<a id="r_ga7e7408507ecdac75cb7c9ba2b9176ec8"></a>

```c
#define DT_INST_PWMS_PERIOD_BY_IDX(inst, idx)
```

相关声明：[DT_INST_PWMS_PERIOD_BY_IDX](../hardware/P264_设备树PWM宏.md#ga7e7408507ecdac75cb7c9ba2b9176ec8)。

等价于 `DT_INST_PWMS_CELL_BY_IDX(inst, idx, period)`。

<a id="r_ga7ac719270232e67f91bc65e3786be1a1"></a>

```c
#define DT_INST_PWMS_PERIOD_BY_NAME(inst, name)
```

相关声明：[DT_INST_PWMS_PERIOD_BY_NAME](../hardware/P264_设备树PWM宏.md#ga7ac719270232e67f91bc65e3786be1a1)。

等价于 `DT_INST_PWMS_CELL_BY_NAME(inst, name, period)`。

<a id="r_ga2b122199764cff41c04bad243f4456dc"></a>

```c
#define DT_INST_PWMS_PERIOD(inst)
```

相关声明：[DT_INST_PWMS_PERIOD](../hardware/P264_设备树PWM宏.md#ga2b122199764cff41c04bad243f4456dc)。

等价于 `DT_INST_PWMS_PERIOD_BY_IDX(inst, 0)`。

<a id="r_ga9cfbc4e3c0ab9d419cfb7700a5b42ced"></a>

```c
#define DT_INST_PWMS_FLAGS_BY_IDX(inst, idx)
```

相关声明：[DT_INST_PWMS_FLAGS_BY_IDX](../hardware/P264_设备树PWM宏.md#ga9cfbc4e3c0ab9d419cfb7700a5b42ced)。

等价于 `DT_INST_PWMS_CELL_BY_IDX(inst, idx, flags)`。

<a id="r_ga23a8815368cbd82a8673e00abdfeab6b"></a>

```c
#define DT_INST_PWMS_FLAGS_BY_NAME(inst, name)
```

相关声明：[DT_INST_PWMS_FLAGS_BY_NAME](../hardware/P264_设备树PWM宏.md#ga23a8815368cbd82a8673e00abdfeab6b)。

等价于 `DT_INST_PWMS_CELL_BY_NAME(inst, name, flags)`。

<a id="r_ga5ca45d33eae6b50012e8c052e3bd5df0"></a>

```c
#define DT_INST_PWMS_FLAGS(inst)
```

相关声明：[DT_INST_PWMS_FLAGS](../hardware/P264_设备树PWM宏.md#ga5ca45d33eae6b50012e8c052e3bd5df0)。

等价于 `DT_INST_PWMS_FLAGS_BY_IDX(inst, 0)`。

## 1.2\_源码定位与版本边界

相对源码定位：[PWM设备树宏](../../../include/zephyr/devicetree/pwms.h)、[PWM绑定常量](../../../include/zephyr/dt-bindings/pwm/pwm.h)、[I2C绑定常量](../../../include/zephyr/dt-bindings/i2c/i2c.h)、[PWM公共绑定](../../../dts/bindings/pwm/pwm-controller.yaml)和[I2C公共绑定](../../../dts/bindings/i2c/i2c-controller.yaml)。官方源码摘要见[来源记录](../SOURCES.md)。

> 译注——源码核对：对象与参数：消费节点的pwms属性引用PWM控制器并携带说明符（Specifier）；CTLR返回节点标识符，不是运行时设备指针。idx为属性条目的逻辑索引，name对应pwm-names名称的小写字母及下划线形式，二者都不是硬件通道号；channel才是说明符中的通道参数单元。参数单元的数目和名字由控制器的具体绑定决定，公共绑定仅要求#pwm-cells，不强制每种控制器都采用相同布局。

> 译注——源码核对：缺省值边界：DT_PWMS_FLAGS_BY_IDX和DT_PWMS_FLAGS_BY_NAME使用DT_PHA_BY_IDX_OR／DT_PHA_BY_NAME_OR，flags不存在时缺省0；普通CELL、CHANNEL、PERIOD读取没有同样的缺省值。尤其当前源码中的DT_INST_PWMS_FLAGS_BY_IDX／BY_NAME直接调用DT_INST_PWMS_CELL_BY_IDX／BY_NAME，并未复用节点版的_OR回退，原始API返回值注释仍声称缺少单元时为0，与当前实际展开存在差异；不能认为两组flags宏在缺少单元时完全等价。

> 译注——源码核对：周期与运行：period读取既有设备树单元，不进行定时器时钟或周期计数换算；按PWM约定其单位为纳秒（Nanoseconds）。宏不会启动波形、设置引脚复用、验证设备就绪或检查目标驱动能否实现该周期。实例inst属于DT_DRV_COMPAT对应的消费节点，不是PWM控制器编号。

> 译注——源码核对：版本边界：本批核对三份官方头文件及PWM、I2C控制器公共绑定并记录摘要；三个源码浏览页的非注释代码与读取的官方原始头文件一致。latest、滚动main与仓库参照版本不自动相同。仓库源码链接仅用于定位；本次没有生成设备树、构建固件或操作硬件。

本次验证范围为文档与源码对照，未编译宏／DTS示例、构建固件或操作硬件。

## 1.3\_原页交叉引用（Cross References）

- [查看此文件的源码](P002_PWM设备树头文件源码.md)
- [DT_PWMS_CTLR_BY_IDX](../hardware/P264_设备树PWM宏.md#ga2f16d00a53717a66668fb8bc967acce5)
- [DT_PWMS_CTLR_BY_NAME](../hardware/P264_设备树PWM宏.md#ga6922e69c707219cd766fe317484dac8a)
- [DT_PWMS_CTLR](../hardware/P264_设备树PWM宏.md#gaff7a0b201d97a1d1bb1893b556d5a194)
- [DT_PWMS_CELL_BY_IDX](../hardware/P264_设备树PWM宏.md#ga0c1ab3329448f92936d57a83b5b3594e)
- [DT_PWMS_CELL_BY_NAME](../hardware/P264_设备树PWM宏.md#ga69233198a489283068bc1ded5072ca26)
- [DT_PWMS_CELL](../hardware/P264_设备树PWM宏.md#ga2062b31a090c05ccd267ae1468b182ef)
- [DT_PWMS_CHANNEL_BY_IDX](../hardware/P264_设备树PWM宏.md#ga10a372e44c7e3feb551ca996c6ca5a8f)
- [DT_PWMS_CHANNEL_BY_NAME](../hardware/P264_设备树PWM宏.md#ga59a4b9884e9620eac04c3808a3a6d164)
- [DT_PWMS_CHANNEL](../hardware/P264_设备树PWM宏.md#gaeb0a10ad37fdfd3dcc75bd379908acdc)
- [DT_PWMS_PERIOD_BY_IDX](../hardware/P264_设备树PWM宏.md#ga9456f65777e6fc7c057c6e0709c9245f)
- [DT_PWMS_PERIOD_BY_NAME](../hardware/P264_设备树PWM宏.md#ga74af83d31fc38f331808dedfaecf4c74)
- [DT_PWMS_PERIOD](../hardware/P264_设备树PWM宏.md#gac6006a723932325b96a1b50619be153b)
- [DT_PWMS_FLAGS_BY_IDX](../hardware/P264_设备树PWM宏.md#gaf9c1ac7f3a39f4022f3ec31ef8de98e6)
- [DT_PWMS_FLAGS_BY_NAME](../hardware/P264_设备树PWM宏.md#ga7a1621bfb223da23aa030b64fc0c0bcd)
- [DT_PWMS_FLAGS](../hardware/P264_设备树PWM宏.md#ga8dcd2d18129504d1a4ab71ae05c48c44)
- [DT_INST_PWMS_CTLR_BY_IDX](../hardware/P264_设备树PWM宏.md#ga4f751ba5f3c1aad5d62178b166f36c24)
- [DT_INST_PWMS_CTLR_BY_NAME](../hardware/P264_设备树PWM宏.md#gae66d3e710496bff9789996ddb72e1ebe)
- [DT_INST_PWMS_CTLR](../hardware/P264_设备树PWM宏.md#ga2f79a0a48e08c89bac58d16d9731e683)
- [DT_INST_PWMS_CELL_BY_IDX](../hardware/P264_设备树PWM宏.md#gad106bf22d9dc90384519cd6ccc8fd1c6)
- [DT_INST_PWMS_CELL_BY_NAME](../hardware/P264_设备树PWM宏.md#ga5731d949be09461f5da040e451cc509c)
- [DT_INST_PWMS_CELL](../hardware/P264_设备树PWM宏.md#ga199804a2d06c301f19c5c8de232ede15)
- [DT_INST_PWMS_CHANNEL_BY_IDX](../hardware/P264_设备树PWM宏.md#ga154ece84d782a7df2ce31b2a34f43870)
- [DT_INST_PWMS_CHANNEL_BY_NAME](../hardware/P264_设备树PWM宏.md#ga60901952d81e29dbfbbe88ee3ffe3e17)
- [DT_INST_PWMS_CHANNEL](../hardware/P264_设备树PWM宏.md#gad871b89fd1b2d62aae84dc35a0819032)
- [DT_INST_PWMS_PERIOD_BY_IDX](../hardware/P264_设备树PWM宏.md#ga7e7408507ecdac75cb7c9ba2b9176ec8)
- [DT_INST_PWMS_PERIOD_BY_NAME](../hardware/P264_设备树PWM宏.md#ga7ac719270232e67f91bc65e3786be1a1)
- [DT_INST_PWMS_PERIOD](../hardware/P264_设备树PWM宏.md#ga2b122199764cff41c04bad243f4456dc)
- [DT_INST_PWMS_FLAGS_BY_IDX](../hardware/P264_设备树PWM宏.md#ga9cfbc4e3c0ab9d419cfb7700a5b42ced)
- [DT_INST_PWMS_FLAGS_BY_NAME](../hardware/P264_设备树PWM宏.md#ga23a8815368cbd82a8673e00abdfeab6b)
- [DT_INST_PWMS_FLAGS](../hardware/P264_设备树PWM宏.md#ga5ca45d33eae6b50012e8c052e3bd5df0)

<a id="header-details"></a>

---

[返回大纲](大纲.md) · [下一章](P002_PWM设备树头文件源码.md)
