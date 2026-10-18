---
id: learning.zephyr-docs.hardware.spidt-0
title: SPI设备树宏
kind: reference
status: maintained
domains: [zephyr, hardware]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__devicetree-spi.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第329章\_SPI设备树宏

原文：[group__devicetree-spi](https://docs.zephyrproject.org/latest/doxygen/html/group__devicetree-spi.html)。读取日期：2026-10-13，`latest`。

## 329.1\_控制器节点与设备节点

本页宏位于 `zephyr/devicetree/spi.h`，从设备树（Devicetree，DT）读取串行外设接口（Serial Peripheral Interface，SPI）的片选（Chip Select，CS）信息。通用输入输出（General-Purpose Input/Output，GPIO）片选通过控制器节点的 `cs-gpios` 属性配置。

参数 `spi` 表示 SPI 总线控制器节点，`spi_dev` 表示挂接在总线上的 SPI 设备节点。设备的 `reg` 地址用于索引控制器的片选列表。实例宏的 `inst` 是 `DT_DRV_COMPAT` 对应兼容类型的实例编号；[`DT_DRV_INST`](../dt_instance_reference/P001_设备树驱动实例宏.md#ga219f413efba2f4c0151468b9a25a8dc1) 宏把它转换为节点标识符，`DT_NODELABEL` 宏按标签选择节点。

以下按原页顺序保留全部展开式和示例。原例的 `...` 是设备树片段中的省略标记，不能把整段当成可直接编译的完整硬件描述。

## 329.2\_实例版本的查询

<a id="ga0ffb7729cd90dc7bf4a1c33ead96a3d8"></a>

`DT_INST_SPI_DEV_CS_GPIOS_CTLR(inst)` 返回该 SPI 设备实例所用片选 GPIO 控制器的节点标识符，等价于：

```c
DT_SPI_DEV_CS_GPIOS_CTLR(DT_DRV_INST(inst))
```

<a id="ga6f42b7305ec5373ae14cad220a3196da"></a>

`DT_INST_SPI_DEV_CS_GPIOS_FLAGS(inst)` 返回片选 GPIO 说明符（GPIO Specifier）中的标志，缺少标志单元（Flags Cell）时为零。说明符在节点引用后列出引脚、标志等数据，单元就是其中由绑定定义的字段。展开为：

```c
DT_SPI_DEV_CS_GPIOS_FLAGS(DT_DRV_INST(inst))
```

<a id="ga1ce1031b612257718fbab08139db44cf"></a>

`DT_INST_SPI_DEV_CS_GPIOS_PIN(inst)` 返回实例片选的 GPIO 引脚号，等价于：

```c
DT_SPI_DEV_CS_GPIOS_PIN(DT_DRV_INST(inst))
```

<a id="ga830f87f79c297c090a1929a288edc7ba"></a>

`DT_INST_SPI_DEV_HAS_CS_GPIOS(inst)` 判断实例的总线是否在其 `DT_INST_REG_ADDR(inst)` 索引处具有片选引脚，有则返回 1，否则返回 0：

```c
DT_SPI_DEV_HAS_CS_GPIOS(DT_DRV_INST(inst))
```

上述四个宏均通过设备节点版本实现，具体属性要求和示例如下。

## 329.3\_查询GPIO控制器

<a id="ga0eaad9de680b5ac7cd8950957560c199"></a>

`DT_SPI_DEV_CS_GPIOS_CTLR(spi_dev)` 返回指定 SPI 设备的片选 GPIO 控制器节点标识符。展开式中，[`DT_BUS`](../dt_node_reference/P001_设备树总线查询宏.md#ga1082d31ac2dafdf9e085d4c23f2169dc) 取得所在总线节点，[`DT_REG_ADDR_RAW`](../dt_reg_reference/P001_设备树寄存器属性宏.md#ga14ebfb75548e45279f3954a75a5f9ac1) 取得用于索引的地址，[`DT_GPIO_CTLR_BY_IDX`](https://docs.zephyrproject.org/latest/doxygen/html/group__devicetree-gpio.html#ga97bd46d2ab88d392a3f336f4d23184eb) 按索引取得 GPIO 控制器：

```c
DT_GPIO_CTLR_BY_IDX(DT_BUS(spi_dev), cs_gpios, DT_REG_ADDR_RAW(spi_dev))
```

原设备树示例包含两个 GPIO 控制器和两个 SPI 设备：

```dts
gpio1: gpio@... { ... };

gpio2: gpio@... { ... };

spi@... {
        compatible = "vnd,spi";
        cs-gpios = <&gpio1 10 GPIO_ACTIVE_LOW>,
                   <&gpio2 20 GPIO_ACTIVE_LOW>;

        a: spi-dev-a@0 {
                reg = <0>;
        };

        b: spi-dev-b@1 {
                reg = <1>;
        };
};
```

调用结果分别为 `gpio1` 和 `gpio2` 节点：

```c
DT_SPI_DEV_CS_GPIOS_CTLR(DT_NODELABEL(a)) // DT_NODELABEL(gpio1)
DT_SPI_DEV_CS_GPIOS_CTLR(DT_NODELABEL(b)) // DT_NODELABEL(gpio2)
```

## 329.4\_查询片选标志

<a id="ga49fd9c174931b44584a7dbbc18f7c644"></a>

`DT_SPI_DEV_CS_GPIOS_FLAGS(spi_dev)` 返回片选 GPIO 标志，展开式使用按索引取标志的 [`DT_GPIO_FLAGS_BY_IDX`](https://docs.zephyrproject.org/latest/doxygen/html/group__devicetree-gpio.html#ga672b2597b99194b8cbd42b3f3401d2b5) 宏：

```c
DT_GPIO_FLAGS_BY_IDX(DT_BUS(spi_dev), cs_gpios, DT_REG_ADDR_RAW(spi_dev))
```

原示例以低电平有效宏 `GPIO_ACTIVE_LOW` 配置片选：

```dts
spi1: spi@... {
        compatible = "vnd,spi";
        cs-gpios = <&gpio1 10 GPIO_ACTIVE_LOW>;

        a: spi-dev-a@0 {
                reg = <0>;
        };
};
```

查询得到该标志：

```c
DT_SPI_DEV_CS_GPIOS_FLAGS(DT_NODELABEL(a)) // GPIO_ACTIVE_LOW
```

如果总线节点 `cs-gpios` 属性中对应设备的 GPIO 说明符没有 `flags` 单元，则展开为零。这里的默认值针对缺少标志单元，不应扩大解释为缺失任意节点、属性或索引时都可安全返回零。

## 329.5\_查询片选引脚号

<a id="ga8c1dd6a65c6f7fdf67291be1ed47fc9f"></a>

`DT_SPI_DEV_CS_GPIOS_PIN(spi_dev)` 返回 SPI 设备片选的 GPIO 引脚号。若总线 `cs-gpios` 属性中对应说明符缺少 `pin` 单元，则是错误。其展开式使用 [`DT_GPIO_PIN_BY_IDX`](https://docs.zephyrproject.org/latest/doxygen/html/group__devicetree-gpio.html#ga8f7d82567056266bab1603865f8b27af) 按索引取引脚：

```c
DT_GPIO_PIN_BY_IDX(DT_BUS(spi_dev), cs_gpios, DT_REG_ADDR_RAW(spi_dev))
```

原设备树如下：

```dts
spi1: spi@... {
        compatible = "vnd,spi";
        cs-gpios = <&gpio1 10 GPIO_ACTIVE_LOW>,
                   <&gpio2 20 GPIO_ACTIVE_LOW>;

        a: spi-dev-a@0 {
                reg = <0>;
        };

        b: spi-dev-b@1 {
                reg = <1>;
        };
};
```

两个设备的查询结果分别为 10 和 20：

```c
DT_SPI_DEV_CS_GPIOS_PIN(DT_NODELABEL(a)) // 10
DT_SPI_DEV_CS_GPIOS_PIN(DT_NODELABEL(b)) // 20
```

## 329.6\_判断设备是否配置GPIO片选

<a id="gad66b759d6aa4826f2c68a94e8708ad4f"></a>

`DT_SPI_DEV_HAS_CS_GPIOS(spi_dev)` 判断某个 SPI 设备是否配置片选。[`DT_PROP_HAS_IDX`](../dt_property_reference/P001_设备树属性读取宏.md#ga479dfc704087eea7e7c5af42ae98576c) 检查属性是否具有指定索引条目：

```c
DT_PROP_HAS_IDX(DT_BUS(spi_dev), cs_gpios, DT_REG_ADDR_RAW(spi_dev))
```

原示例第一条总线为两个设备配置片选，第二条总线没有该属性：

```dts
spi1: spi@... {
        compatible = "vnd,spi";
        cs-gpios = <&gpio1 10 GPIO_ACTIVE_LOW>,
                   <&gpio2 20 GPIO_ACTIVE_LOW>;

        a: spi-dev-a@0 {
                reg = <0>;
        };

        b: spi-dev-b@1 {
                reg = <1>;
        };
};

spi2: spi@... {
        compatible = "vnd,spi";
        c: spi-dev-c@0 {
                reg = <0>;
        };
};
```

因此设备 `a`、`b` 返回 1，设备 `c` 返回 0：

```c
DT_SPI_DEV_HAS_CS_GPIOS(DT_NODELABEL(a)) // 1
DT_SPI_DEV_HAS_CS_GPIOS(DT_NODELABEL(b)) // 1
DT_SPI_DEV_HAS_CS_GPIOS(DT_NODELABEL(c)) // 0
```

返回条件是设备所在总线节点 `DT_BUS(spi_dev)` 在设备地址对应索引处具有片选引脚；否则为 0。原描述写作 `DT_REG_ADDR(spi_dev)`，展开式使用 `DT_REG_ADDR_RAW(spi_dev)`，这里保持原展开式。

## 329.7\_判断控制器属性并统计片选数

<a id="gae8db0ce095bdd0066a845bc6a9bf329d"></a>

`DT_SPI_HAS_CS_GPIOS(spi)` 判断 SPI 控制器节点是否具有 `cs-gpios` 属性。该属性是节点引用及参数数组（Phandle Array），用于指定片选线。[`DT_NODE_HAS_PROP`](../dt_identity_reference/P002_设备树存在性与状态宏.md#gacce67bf20541cd2d07d8540058964692) 是检查节点属性是否存在的宏：

```c
DT_NODE_HAS_PROP(spi, cs_gpios)
```

原设备树中只有 `spi1` 配置了片选：

```dts
spi1: spi@... {
        compatible = "vnd,spi";
        cs-gpios = <&gpio1 10 GPIO_ACTIVE_LOW>,
                   <&gpio2 20 GPIO_ACTIVE_LOW>;
};

spi2: spi@... {
        compatible = "vnd,spi";
};
```

所以结果分别为 1 和 0：

```c
DT_SPI_HAS_CS_GPIOS(DT_NODELABEL(spi1)) // 1
DT_SPI_HAS_CS_GPIOS(DT_NODELABEL(spi2)) // 0
```

<a id="gafe2bddd961fe08672e131cfbd73eb466"></a>

`DT_SPI_NUM_CS_GPIOS(spi)` 返回控制器 `cs-gpios` 属性的逻辑长度，也就是配置的片选 GPIO 数量；没有该属性时返回 0。[`COND_CODE_1`](../util_reference/P001_通用工具公共接口.md#ga358bc3e7669c860a98839a51cd526b20) 根据条件选择展开分支，[`DT_PROP_LEN`](../dt_property_reference/P001_设备树属性读取宏.md#gaa7f5afcedd1f54be79a5337e8e28a5b6) 取得属性长度：

```c
COND_CODE_1(DT_SPI_HAS_CS_GPIOS(spi), \
            (DT_PROP_LEN(spi, cs_gpios)), (0))
```

原例仍为一条总线具有两条片选，另一条没有片选属性：

```dts
spi1: spi@... {
        compatible = "vnd,spi";
        cs-gpios = <&gpio1 10 GPIO_ACTIVE_LOW>,
                   <&gpio2 20 GPIO_ACTIVE_LOW>;
};

spi2: spi@... {
        compatible = "vnd,spi";
};
```

结果分别为 2 和 0：

```c
DT_SPI_NUM_CS_GPIOS(DT_NODELABEL(spi1)) // 2
DT_SPI_NUM_CS_GPIOS(DT_NODELABEL(spi2)) // 0
```

---

[上一章：SPI模拟函数表](P328_SPI模拟函数表.md) · [下一章：UART公共接口](P330_UART公共接口.md) · [返回大纲](大纲.md)
