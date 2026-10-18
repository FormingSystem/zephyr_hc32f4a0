---
id: learning.zephyr-docs.hardware.i2cbackend-2
title: I2CEEPROM目标接口
kind: reference
status: maintained
domains: [zephyr, hardware]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__i2c__eeprom__target__api.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第313章\_I2CEEPROM目标接口

原文：[group__i2c__eeprom__target__api](https://docs.zephyrproject.org/latest/doxygen/html/group__i2c__eeprom__target__api.html)。读取日期：2026-10-13，`latest`。

<a id="details"></a>
<a id="doc-func-members"></a>
<a id="doc-typedef-members"></a>
<a id="func-members"></a>
<a id="header-details"></a>
<a id="header-doc-func-members"></a>
<a id="header-doc-typedef-members"></a>
<a id="header-func-members"></a>
<a id="header-typedef-members"></a>
<a id="typedef-members"></a>

## 313.1\_虚拟存储器与变更回调

本页提供集成电路间总线（Inter-Integrated Circuit，I²C）电可擦可编程只读存储器（Electrically Erasable Programmable Read-Only Memory，EEPROM）目标设备接口，自Zephyr 1.13提供，版本为1.0.0。声明来自 `zephyr/drivers/i2c/target/eeprom.h`。

这里操作的是虚拟EEPROM（Virtual EEPROM）。所有函数的 `dev` 均指向驱动实例的设备结构。应用变更回调（Change Callback）类型为：

<a id="ga769f4b319013956d58fdc56d378519aa"></a>
<a id="r_ga769f4b319013956d58fdc56d378519aa"></a>

```c
typedef void (*eeprom_target_changed_handler_t)(const struct device *dev,
                                               void *user_data);
```

`user_data` 为设置回调时提供的可选用户数据。

<a id="ga3da67a267034e3b90c1a7c84588c3839"></a>
<a id="r_ga3da67a267034e3b90c1a7c84588c3839"></a>

## 313.2\_eeprom_target_get_size

函数 [`eeprom_target_get_size()`](https://docs.zephyrproject.org/latest/doxygen/html/group__i2c__eeprom__target__api.html#ga3da67a267034e3b90c1a7c84588c3839) 声明为：

```c
size_t eeprom_target_get_size(const struct device * dev);
```

取得虚拟EEPROM大小，返回值单位为字节。

<a id="ga8c2d7c18fcec4ce2241850f031966a89"></a>
<a id="r_ga8c2d7c18fcec4ce2241850f031966a89"></a>

## 313.3\_eeprom_target_program

函数 [`eeprom_target_program()`](https://docs.zephyrproject.org/latest/doxygen/html/group__i2c__eeprom__target__api.html#ga8c2d7c18fcec4ce2241850f031966a89) 声明为：

```c
static inline int eeprom_target_program(const struct device * dev, const uint8_t * eeprom_data, unsigned int length);
```

编程虚拟EEPROM存储内容。**此接口已弃用，应改用 [`eeprom_target_write_data()`](https://docs.zephyrproject.org/latest/doxygen/html/group__i2c__eeprom__target__api.html#gad562c9ac13d3fa7a7b43c1d8ba415f11)。**`eeprom_data` 指向待编程数据，`length` 为数据长度。成功返回 `0`，数据大小无效返回 `-EINVAL`。

<a id="ga72b88bc1df1ec097ed677f94e9dad875"></a>
<a id="r_ga72b88bc1df1ec097ed677f94e9dad875"></a>

## 313.4\_eeprom_target_read

函数 [`eeprom_target_read()`](https://docs.zephyrproject.org/latest/doxygen/html/group__i2c__eeprom__target__api.html#ga72b88bc1df1ec097ed677f94e9dad875) 声明为：

```c
static inline int eeprom_target_read(const struct device * dev, uint8_t * eeprom_data, unsigned int offset);
```

读取虚拟EEPROM中的单个字节。`eeprom_data` 指向保存字节的位置，`offset` 为待读字节相对存储起始位置的偏移。成功返回 `0`，数据指针或偏移无效返回 `-EINVAL`。

<a id="ga1543dbc12e26df856eac01b1a686d7c5"></a>
<a id="r_ga1543dbc12e26df856eac01b1a686d7c5"></a>

## 313.5\_eeprom_target_read_data

函数 [`eeprom_target_read_data()`](https://docs.zephyrproject.org/latest/doxygen/html/group__i2c__eeprom__target__api.html#ga1543dbc12e26df856eac01b1a686d7c5) 声明为：

```c
int eeprom_target_read_data(const struct device * dev, off_t offset, void * data, size_t len);
```

从虚拟EEPROM读取数据。`offset` 为起始地址偏移，`data` 指向接收缓冲区，`len` 为读取字节数。成功返回 `0`，失败返回负错误码。

<a id="ga802f5d779e9a837a81b8b617037dfce8"></a>
<a id="r_ga802f5d779e9a837a81b8b617037dfce8"></a>

## 313.6\_eeprom_target_set_addr

函数 [`eeprom_target_set_addr()`](https://docs.zephyrproject.org/latest/doxygen/html/group__i2c__eeprom__target__api.html#ga802f5d779e9a837a81b8b617037dfce8) 声明为：

```c
int eeprom_target_set_addr(const struct device * dev, uint8_t addr);
```

运行时改变EEPROM目标设备地址，`addr` 为新地址。成功返回 `0`；参数无效返回 `-EINVAL`；目标注册中的一般输入/输出（Input/Output，I/O）错误返回 `-EIO`；未实现目标模式返回 `-ENOSYS`。

> 译注：原错误说明把注册函数拼作 `i2c_taget_register`，此处记录原拼写问题，对应公共接口名称为 `i2c_target_register()`。

> 译注——实现条件：本次核对的 `eeprom_target.c` 仅在启用 `CONFIG_I2C_EEPROM_TARGET_RUNTIME_ADDR` 时定义 `eeprom_target_set_addr()`。头文件无条件声明该函数，不表示所有构建均有相应实现。相对源码见 [eeprom_target.c](../../../drivers/i2c/target/eeprom_target.c)，官方快照依据见[目标EEPROM头文件参考](../flash_reference/P025_I2C目标EEPROM头文件参考.md)。

<a id="gaab87512e92f7f50b93019c5f9255c4a7"></a>
<a id="r_gaab87512e92f7f50b93019c5f9255c4a7"></a>

## 313.7\_eeprom_target_set_changed_callback

函数 [`eeprom_target_set_changed_callback()`](https://docs.zephyrproject.org/latest/doxygen/html/group__i2c__eeprom__target__api.html#gaab87512e92f7f50b93019c5f9255c4a7) 声明为：

```c
void eeprom_target_set_changed_callback(const struct device * dev, eeprom_target_changed_handler_t handler, void * user_data);
```

设置EEPROM变更处理函数。`handler` 是EEPROM发生变化时调用的处理函数，`user_data` 为传给回调的可选用户数据。没有返回值。

<a id="gad562c9ac13d3fa7a7b43c1d8ba415f11"></a>
<a id="r_gad562c9ac13d3fa7a7b43c1d8ba415f11"></a>

## 313.8\_eeprom_target_write_data

函数 [`eeprom_target_write_data()`](https://docs.zephyrproject.org/latest/doxygen/html/group__i2c__eeprom__target__api.html#gad562c9ac13d3fa7a7b43c1d8ba415f11) 声明为：

```c
int eeprom_target_write_data(const struct device * dev, off_t offset, const void * data, size_t len);
```

向虚拟EEPROM写入数据。`offset` 为写入地址偏移，`data` 指向源缓冲区，`len` 为写入字节数。成功返回 `0`，失败返回负错误码。


---

[上一章：I2C驱动函数表](P312_I2C驱动函数表.md) · [下一章：I2C模拟后端](P314_I2C模拟后端.md) · [返回大纲](大纲.md)
