---
id: learning.zephyr-docs.hardware.emulbus-1
title: eSPI总线仿真接口
kind: reference
status: maintained
domains: [zephyr, hardware]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__espi__emul__interface.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第486章\_eSPI总线仿真接口

原文：[group__espi__emul__interface](P486_eSPI总线仿真接口.md)。读取日期：2026-10-13，`latest`。

本页介绍**增强型串行外设接口（Enhanced Serial Peripheral Interface，eSPI）**的仿真接口。主头文件为 `zephyr/drivers/espi_emul.h`，提供设备及控制器仿真的**应用程序编程接口（Application Programming Interface，API）**。

## 486.1\_设备、控制器和片选

[`emul_espi_device_api`](P481_eSPI仿真设备API结构.md) 定义设备仿真器 API；[`espi_emul`](P488_eSPI仿真器链表节点.md) 是 eSPI 设备仿真器链表中的节点；[`emul_espi_driver_api`](P482_eSPI仿真驱动API结构.md) 定义控制器仿真器 API。**片选（Chip Select）**用于指定总线上的目标，主机片选宏保留如下：

```c
#define EMUL_ESPI_HOST_CHIPSEL 0
```

下面各回调和函数均由上述头文件声明。文中 `-EIO` 表示通用**输入/输出错误（Input/Output Error）**，`NULL` 表示空指针；二者分别用于整数错误返回和指针查找结果。

## 486.2\_虚拟线读写回调

**虚拟线（Virtual Wire，VW）**是在 eSPI 上传递的信号状态。设置与读取请求以虚拟线数据包交给设备仿真器，分别使用以下函数指针类型。

```c
typedef int (*emul_espi_api_set_vw)(const struct emul *target,
                                     enum espi_vwire_signal vw,
                                     uint8_t level);
```

[`emul_espi_api_set_vw`](P486_eSPI总线仿真接口.md) 将虚拟线设置请求交给仿真器，仿真器据此更新其虚拟线的状态，即电平（Level）。参数 `target` 是设备仿真器实例，`vw` 是待设置的信号，`level` 是要求的电平：低电平 `LOW(0)` 或高电平 `HIGH(1)`。成功返回 `0`，通用输入/输出错误返回 `-EIO`。

```c
typedef int (*emul_espi_api_get_vw)(const struct emul *target,
                                     enum espi_vwire_signal vw,
                                     uint8_t *level);
```

[`emul_espi_api_get_vw`](P486_eSPI总线仿真接口.md) 将虚拟线读取请求交给仿真器，仿真器返回该虚拟线的状态。`target` 是设备仿真器实例，`vw` 是要读取的信号，`level` 指向用于取得信号电平的变量。成功返回 `0`，通用输入/输出错误返回 `-EIO`。

## 486.3\_共享内存地址回调

**高级配置与电源接口（Advanced Configuration and Power Interface，ACPI）**的**共享内存（Shared Memory，SHM）**地址通过下面的回调取得。

```c
typedef uintptr_t (*emul_espi_api_get_acpi_shm)(const struct emul *target);
```

[`emul_espi_api_get_acpi_shm`](P486_eSPI总线仿真接口.md) 返回仿真器拥有的 ACPI 共享内存地址。参数 `target` 是设备仿真器实例，返回值为内存地址，类型 [`uintptr_t`](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a4788399d1d0b37ccf098a7da82254808) 是可表示指针值的无符号整数类型。

**注意：**只有启用 Kconfig 配置项 [`CONFIG_ESPI_PERIPHERAL_ACPI_SHM_REGION`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ESPI_PERIPHERAL_ACPI_SHM_REGION)，该接口才可用；这一配置启用 eSPI 外设的 ACPI 共享内存区域支持。

## 486.4\_查找仿真器与触发事件回调

[`emul_find_emul`](P486_eSPI总线仿真接口.md) 查找 eSPI 总线上存在的仿真器。原文说明，目前它只用于查找主机设备的仿真器，在带有**串行外设接口闪存（Serial Peripheral Interface Flash，SPI Flash）**芯片的系统中也可能有用。

```c
typedef struct espi_emul *(*emul_find_emul)(const struct device *dev,
                                           unsigned int chipsel);
```

`dev` 为 eSPI 仿真控制器设备，`chipsel` 为片选值。返回可使用的 [`espi_emul`](P488_eSPI仿真器链表节点.md) 指针；找不到时返回 `NULL`。

[`emul_trigger_event`](P486_eSPI总线仿真接口.md) 在 eSPI 控制器侧的仿真器上触发事件，从而调用相应的**回调（Callback）**函数。

```c
typedef int (*emul_trigger_event)(const struct device *dev,
                                   struct espi_event *evt);
```

`dev` 是被仿真的 eSPI 控制器设备实例，`evt` 是待触发事件。成功返回 `0`；通用输入/输出错误返回 `-EIO`。

## 486.5\_注册设备与模拟主机操作

[`espi_emul_register()`](P486_eSPI总线仿真接口.md) 在控制器上注册被仿真的设备。

```c
int espi_emul_register(const struct device *dev, struct espi_emul *emul);
```

参数 `dev` 是将使用仿真器的设备，[`emul`](P477_仿真器实例结构.md) 是要使用的 eSPI 仿真器。原页明确说明：**总是返回 `0`，表示成功**。

注册后可通过主机侧辅助函数设置虚拟线或写入端口。[`emul_espi_host_send_vw()`](P486_eSPI总线仿真接口.md) 设置主机侧的 eSPI 虚拟线，并在被仿真的 eSPI 控制器上触发相应事件及回调。

```c
int emul_espi_host_send_vw(const struct device *espi_dev,
                           enum espi_vwire_signal vw, uint8_t level);
```

`espi_dev` 是 eSPI 仿真控制器设备，`vw` 是要设置的信号，`level` 是所需电平。成功返回 `0`；通用输入/输出错误返回 `-EIO`。

[`emul_espi_host_port80_write()`](P486_eSPI总线仿真接口.md) 在仿真的主机侧执行端口 80 写入操作，并在被仿真的 eSPI 控制器上触发相应事件及回调。

```c
int emul_espi_host_port80_write(const struct device *espi_dev, uint32_t data);
```

`espi_dev` 是 eSPI 仿真控制器设备，`data` 是待写入数据。成功返回 `0`；通用输入/输出错误返回 `-EIO`。

> 译注：原文 `data` 参数描述中的 “date” 按上下文译为“数据”。“port80” 保留为接口中的端口名称，不改变函数名。

## 486.6\_取得主机共享内存

[`emul_espi_host_get_acpi_shm()`](P486_eSPI总线仿真接口.md) 返回主机设备 ACPI 共享内存区域的起始地址。

```c
uintptr_t emul_espi_host_get_acpi_shm(const struct device *espi_dev);
```

参数 `espi_dev` 是 eSPI 仿真控制器设备。区域大小由 `CONFIG_EMUL_ESPI_HOST_ACPI_SHM_REGION_SIZE` 配置项决定；返回值为 ACPI 共享内存起始地址。

**注意：**和共享内存地址回调一样，只有启用 [`CONFIG_ESPI_PERIPHERAL_ACPI_SHM_REGION`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ESPI_PERIPHERAL_ACPI_SHM_REGION) 时，这个函数才可用。

---

[上一章：仿真器总线联合体](P485_仿真器总线联合体.md) · [下一章：MSPI总线仿真接口](P487_MSPI总线仿真接口.md) · [返回大纲](大纲.md)
