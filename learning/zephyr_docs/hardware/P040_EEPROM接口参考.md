---
id: learning.zephyr-docs.hardware.hwapi-eeprom
title: EEPROM接口参考
kind: reference
status: maintained
domains: [zephyr, hardware]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__eeprom__interface.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第40章\_EEPROM接口参考

原文：[group__eeprom__interface](https://docs.zephyrproject.org/latest/doxygen/html/group__eeprom__interface.html)。读取日期：2026-10-13，`latest`。

<a id="details"></a>
<a id="doc-func-members"></a>
<a id="files"></a>
<a id="func-members"></a>
<a id="groups"></a>
<a id="header-details"></a>
<a id="header-doc-func-members"></a>
<a id="header-files"></a>
<a id="header-func-members"></a>
<a id="header-groups"></a>
<a id="r_eeprom_2Eh"></a>
<a id="r_eeprom_5Ffake"></a>
<a id="r_eeprom_5Finterface_5Fbackend"></a>

## 40.1\_公共接口与版本

**电可擦可编程只读存储器（Electrically Erasable Programmable Read-Only Memory，EEPROM）**的 **应用程序编程接口（Application Programming Interface，API）**提供读、写和容量查询。接口自Zephyr 2.1引入，版本为1.0.0；官方公共头文件为 `zephyr/drivers/eeprom.h`。概览与配置见[EEPROM接口](P036_EEPROM接口.md)。

原页还列出[EEPROM驱动后端API](P049_EEPROM驱动后端接口.md)和[伪EEPROM驱动（Fake EEPROM）](P051_伪EEPROM接口.md)两个主题。后者用于模拟设备行为，不表示读写真实器件已经通过验证。

## 40.2\_读取和写入

[`eeprom_read()`](https://docs.zephyrproject.org/latest/doxygen/html/group__eeprom__interface.html#ga92b92c8fb721f1b94038a20443d46e52) 从EEPROM读取数据，[`eeprom_write()`](https://docs.zephyrproject.org/latest/doxygen/html/group__eeprom__interface.html#ga1973e8982de88f53e49154dc73461e56) 向EEPROM写入数据。

<a id="ga92b92c8fb721f1b94038a20443d46e52"></a>
<a id="r_ga92b92c8fb721f1b94038a20443d46e52"></a>
<a id="ga1973e8982de88f53e49154dc73461e56"></a>
<a id="r_ga1973e8982de88f53e49154dc73461e56"></a>

```c
int eeprom_read(const struct device *dev, off_t offset,
                void *data, size_t len);
int eeprom_write(const struct device *dev, off_t offset,
                 const void *data, size_t len);
```

| 参数 | 读取时的含义 | 写入时的含义 |
| --- | --- | --- |
| `dev` | EEPROM设备指针。 | EEPROM设备指针。 |
| `offset` | 读取起始偏移。 | 写入起始偏移。 |
| `data` | 接收读出数据的缓冲区。 | 保存待写入数据的缓冲区。 |
| `len` | 要读取的字节数。 | 要写入的字节数。 |

两个函数成功返回0，失败返回负错误码。这里的返回值是操作状态，不能将它解释为实际读写字节数。

## 40.3\_查询容量

[`eeprom_get_size()`](https://docs.zephyrproject.org/latest/doxygen/html/group__eeprom__interface.html#ga27a1f50af8916f9291dad4a63796a707) 返回EEPROM容量：

<a id="ga27a1f50af8916f9291dad4a63796a707"></a>
<a id="r_ga27a1f50af8916f9291dad4a63796a707"></a>

```c
size_t eeprom_get_size(const struct device *dev);
```

`dev` 为EEPROM设备指针；返回值以字节为单位，属于容量而非上一节的成功或失败状态。结合[EEPROM计数示例](P043_EEPROM计数示例.md)，可以看到设备查找、容量输出和持久化启动计数的使用方式。

对应的完整[头文件参考](../flash_reference/P021_EEPROM公共头文件参考.md)和[源码浏览译文](../flash_reference/P022_EEPROM公共头文件源码.md)已补齐，类型、条件声明和调用转发可继续对照。

[上一章：熵源接口参考](P039_熵源接口参考.md) · [下一章：CAN收发器接口参考](P041_CAN收发器接口参考.md) · [返回大纲](大纲.md)
