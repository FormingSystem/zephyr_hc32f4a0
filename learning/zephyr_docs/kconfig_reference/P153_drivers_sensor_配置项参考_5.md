---
id: learning.zephyr-docs.kconfig-reference.page-153
title: "`drivers/sensor`配置项参考（5/15）"
kind: reference
status: evolving
domains: [zephyr, kconfig, configuration]
source_url: https://docs.zephyrproject.org/latest/kconfig.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；分册、相对路径和明确标注的译注为本地新增。 -->

# 第153章\_`drivers/sensor`配置项参考（5/15）

本章翻译官方 Kconfig 数据库中 `drivers/sensor` 的 100 条定义记录。提示（Prompt）、帮助（Help）与菜单路径均已翻译；条件表达式、默认值和配置标识符保留原值。原页：[Kconfig Search](https://docs.zephyrproject.org/latest/kconfig.html)。来源数据库版本为 `main`，快照摘要与完整覆盖范围见[本册大纲](大纲.md)。

`main` 源码链接随上游变化；行号来自本次数据库快照，不能视为固定提交定位。无提示的配置项保留其不可直接由用户赋值的属性。原库中存在未收录定义的交叉引用，本章在对应位置明确标出。

<a id="CONFIG_DHT20_CRC"></a>

## 153.1 `CONFIG_DHT20_CRC`

**提示（Prompt）**：使用循环冗余校验（CRC）错误检测

**说明（Help）**

校验接收数据（RX Data）中的 CRC 字节。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_DHT20 && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
n
```

**主动选择（Selects）**

```text
CONFIG_CRC
```

**定义位置（Location）**：[`drivers/sensor/aosong/dht20/Kconfig:19`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/aosong/dht20/Kconfig#L19)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → DHT20 / AHT20 / AM2301B 温湿度传感器（Temperature and Humidity Sensor）

**配置项引用（Symbol References）**：[`CONFIG_DHT20`](P152_drivers_sensor_配置项参考_4.md#CONFIG_DHT20)、[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)、[`CONFIG_CRC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_CRC)。

<a id="CONFIG_DHT_LOCK_IRQS"></a>

## 153.2 `CONFIG_DHT_LOCK_IRQS`

**提示（Prompt）**：传感器测量期间锁定中断请求（IRQ）

**说明（Help）**

在读取传感器时锁定中断请求（IRQ），可显著提高成功取得读数的概率，但会延迟中断服务，例如蓝牙（Bluetooth）中断服务。注意，其他系统可能需要相应调整以适应此行为。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_DHT && CONFIG_SENSOR
```

**定义位置（Location）**：[`drivers/sensor/aosong/dht/Kconfig:16`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/aosong/dht/Kconfig#L16)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → DHT 温湿度传感器（Temperature and Humidity Sensor）

**配置项引用（Symbol References）**：[`CONFIG_DHT`](P152_drivers_sensor_配置项参考_4.md#CONFIG_DHT)、[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)。

<a id="CONFIG_DPS310"></a>

## 153.3 `CONFIG_DPS310`

**提示（Prompt）**：DPS310 传感器（Sensor）

**说明（Help）**

启用基于 I2C 的 DPS310 温度和压力传感器（Temperature and Pressure Sensor）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_INFINEON_DPS310_ENABLED && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_I2C
```

**定义位置（Location）**：[`drivers/sensor/infineon/dps310/Kconfig:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/infineon/dps310/Kconfig#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)、[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)。

<a id="CONFIG_DPS310_PRESS_OSR_128X"></a>

## 153.4 `CONFIG_DPS310_PRESS_OSR_128X`

**提示（Prompt）**：128 倍（x128）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`drivers/sensor/infineon/dps310/Kconfig:64`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/infineon/dps310/Kconfig#L64)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → DPS310 传感器（Sensor） → 属性（Attributes） → DPS310 压力过采样（Pressure Oversampling）

<a id="CONFIG_DPS310_PRESS_OSR_16X"></a>

## 153.5 `CONFIG_DPS310_PRESS_OSR_16X`

**提示（Prompt）**：16 倍（x16）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`drivers/sensor/infineon/dps310/Kconfig:58`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/infineon/dps310/Kconfig#L58)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → DPS310 传感器（Sensor） → 属性（Attributes） → DPS310 压力过采样（Pressure Oversampling）

<a id="CONFIG_DPS310_PRESS_OSR_1X"></a>

## 153.6 `CONFIG_DPS310_PRESS_OSR_1X`

**提示（Prompt）**：1 倍（x1）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`drivers/sensor/infineon/dps310/Kconfig:50`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/infineon/dps310/Kconfig#L50)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → DPS310 传感器（Sensor） → 属性（Attributes） → DPS310 压力过采样（Pressure Oversampling）

<a id="CONFIG_DPS310_PRESS_OSR_2X"></a>

## 153.7 `CONFIG_DPS310_PRESS_OSR_2X`

**提示（Prompt）**：2 倍（x2）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`drivers/sensor/infineon/dps310/Kconfig:52`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/infineon/dps310/Kconfig#L52)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → DPS310 传感器（Sensor） → 属性（Attributes） → DPS310 压力过采样（Pressure Oversampling）

<a id="CONFIG_DPS310_PRESS_OSR_32X"></a>

## 153.8 `CONFIG_DPS310_PRESS_OSR_32X`

**提示（Prompt）**：32 倍（x32）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`drivers/sensor/infineon/dps310/Kconfig:60`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/infineon/dps310/Kconfig#L60)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → DPS310 传感器（Sensor） → 属性（Attributes） → DPS310 压力过采样（Pressure Oversampling）

<a id="CONFIG_DPS310_PRESS_OSR_4X"></a>

## 153.9 `CONFIG_DPS310_PRESS_OSR_4X`

**提示（Prompt）**：4 倍（x4）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`drivers/sensor/infineon/dps310/Kconfig:54`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/infineon/dps310/Kconfig#L54)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → DPS310 传感器（Sensor） → 属性（Attributes） → DPS310 压力过采样（Pressure Oversampling）

<a id="CONFIG_DPS310_PRESS_OSR_64X"></a>

## 153.10 `CONFIG_DPS310_PRESS_OSR_64X`

**提示（Prompt）**：64 倍（x64）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`drivers/sensor/infineon/dps310/Kconfig:62`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/infineon/dps310/Kconfig#L62)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → DPS310 传感器（Sensor） → 属性（Attributes） → DPS310 压力过采样（Pressure Oversampling）

<a id="CONFIG_DPS310_PRESS_OSR_8X"></a>

## 153.11 `CONFIG_DPS310_PRESS_OSR_8X`

**提示（Prompt）**：8 倍（x8）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`drivers/sensor/infineon/dps310/Kconfig:56`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/infineon/dps310/Kconfig#L56)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → DPS310 传感器（Sensor） → 属性（Attributes） → DPS310 压力过采样（Pressure Oversampling）

<a id="CONFIG_DPS310_TEMP_OSR_128X"></a>

## 153.12 `CONFIG_DPS310_TEMP_OSR_128X`

**提示（Prompt）**：128 倍（x128）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`drivers/sensor/infineon/dps310/Kconfig:40`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/infineon/dps310/Kconfig#L40)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → DPS310 传感器（Sensor） → 属性（Attributes） → DPS310 温度过采样（Temperature Oversampling）

<a id="CONFIG_DPS310_TEMP_OSR_16X"></a>

## 153.13 `CONFIG_DPS310_TEMP_OSR_16X`

**提示（Prompt）**：16 倍（x16）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`drivers/sensor/infineon/dps310/Kconfig:34`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/infineon/dps310/Kconfig#L34)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → DPS310 传感器（Sensor） → 属性（Attributes） → DPS310 温度过采样（Temperature Oversampling）

<a id="CONFIG_DPS310_TEMP_OSR_1X"></a>

## 153.14 `CONFIG_DPS310_TEMP_OSR_1X`

**提示（Prompt）**：1 倍（x1）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`drivers/sensor/infineon/dps310/Kconfig:26`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/infineon/dps310/Kconfig#L26)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → DPS310 传感器（Sensor） → 属性（Attributes） → DPS310 温度过采样（Temperature Oversampling）

<a id="CONFIG_DPS310_TEMP_OSR_2X"></a>

## 153.15 `CONFIG_DPS310_TEMP_OSR_2X`

**提示（Prompt）**：2 倍（x2）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`drivers/sensor/infineon/dps310/Kconfig:28`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/infineon/dps310/Kconfig#L28)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → DPS310 传感器（Sensor） → 属性（Attributes） → DPS310 温度过采样（Temperature Oversampling）

<a id="CONFIG_DPS310_TEMP_OSR_32X"></a>

## 153.16 `CONFIG_DPS310_TEMP_OSR_32X`

**提示（Prompt）**：32 倍（x32）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`drivers/sensor/infineon/dps310/Kconfig:36`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/infineon/dps310/Kconfig#L36)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → DPS310 传感器（Sensor） → 属性（Attributes） → DPS310 温度过采样（Temperature Oversampling）

<a id="CONFIG_DPS310_TEMP_OSR_4X"></a>

## 153.17 `CONFIG_DPS310_TEMP_OSR_4X`

**提示（Prompt）**：4 倍（x4）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`drivers/sensor/infineon/dps310/Kconfig:30`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/infineon/dps310/Kconfig#L30)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → DPS310 传感器（Sensor） → 属性（Attributes） → DPS310 温度过采样（Temperature Oversampling）

<a id="CONFIG_DPS310_TEMP_OSR_64X"></a>

## 153.18 `CONFIG_DPS310_TEMP_OSR_64X`

**提示（Prompt）**：64 倍（x64）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`drivers/sensor/infineon/dps310/Kconfig:38`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/infineon/dps310/Kconfig#L38)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → DPS310 传感器（Sensor） → 属性（Attributes） → DPS310 温度过采样（Temperature Oversampling）

<a id="CONFIG_DPS310_TEMP_OSR_8X"></a>

## 153.19 `CONFIG_DPS310_TEMP_OSR_8X`

**提示（Prompt）**：8 倍（x8）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`drivers/sensor/infineon/dps310/Kconfig:32`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/infineon/dps310/Kconfig#L32)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → DPS310 传感器（Sensor） → 属性（Attributes） → DPS310 温度过采样（Temperature Oversampling）

<a id="CONFIG_DS18B20"></a>

## 153.20 `CONFIG_DS18B20`

**提示（Prompt）**：DS18B20 温度传感器（Temperature Sensor）

**说明（Help）**

启用 DS18B20 单总线（1-Wire）温度传感器驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(DT_HAS_MAXIM_DS18B20_ENABLED || DT_HAS_MAXIM_DS18S20_ENABLED) && CONFIG_W1_NET && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/sensor/maxim/ds18b20/Kconfig:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/maxim/ds18b20/Kconfig#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers）

**配置项引用（Symbol References）**：[`CONFIG_W1_NET`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_W1_NET)、[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)。

<a id="CONFIG_EMUL_ADLTC2990"></a>

## 153.21 `CONFIG_EMUL_ADLTC2990`

**提示（Prompt）**：ADLTC2990 仿真器（Emulator）

**说明（Help）**

启用 ADLTC2990 仿真器（Emulator）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ADLTC2990 && CONFIG_EMUL && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/sensor/adi/adltc2990/Kconfig:15`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/adi/adltc2990/Kconfig#L15)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → ADLTC2990 四通道 I²C 电压、电流和温度监视器（Monitor）

**配置项引用（Symbol References）**：[`CONFIG_ADLTC2990`](P149_drivers_sensor_配置项参考_1.md#CONFIG_ADLTC2990)、[`CONFIG_EMUL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_EMUL)、[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)。

<a id="CONFIG_EMUL_AKM09918C"></a>

## 153.22 `CONFIG_EMUL_AKM09918C`

**提示（Prompt）**：AKM09918C 仿真器（Emulator）

**说明（Help）**

启用 AKM09918C 硬件仿真器（Hardware Emulator），以便在 `native_sim` 和 QEMU 中测试该磁力计（Magnetometer）的传感器 API。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_AKM09918C && CONFIG_EMUL && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/sensor/asahi_kasei/akm09918c/Kconfig:15`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/asahi_kasei/akm09918c/Kconfig#L15)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → AKM09918C 磁力计

**配置项引用（Symbol References）**：[`CONFIG_AKM09918C`](P150_drivers_sensor_配置项参考_2.md#CONFIG_AKM09918C)、[`CONFIG_EMUL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_EMUL)、[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)。

<a id="CONFIG_EMUL_AMD_SB_TSI"></a>

## 153.23 `CONFIG_EMUL_AMD_SB_TSI`

**提示（Prompt）**：AMD SB-TSI 仿真器（Emulator）

**说明（Help）**

启用 AMD SB-TSI 硬件仿真器（Hardware Emulator）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_AMD_SB_TSI && CONFIG_EMUL && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/sensor/amd_sb_tsi/Kconfig:15`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/amd_sb_tsi/Kconfig#L15)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → AMD SB 温度传感器接口（Temperature Sensor Interface）

**配置项引用（Symbol References）**：[`CONFIG_AMD_SB_TSI`](P150_drivers_sensor_配置项参考_2.md#CONFIG_AMD_SB_TSI)、[`CONFIG_EMUL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_EMUL)、[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)。

<a id="CONFIG_EMUL_BMA4XX"></a>

## 153.24 `CONFIG_EMUL_BMA4XX`

**提示（Prompt）**：BMA4XX 仿真器（Emulator）

**说明（Help）**

启用 BMA4XX 硬件仿真器（Hardware Emulator），以便在 `native_sim` 和 QEMU 中测试该传感器的传感器 API。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_EMUL && CONFIG_BMA4XX && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/sensor/bosch/bma4xx/Kconfig:29`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/bosch/bma4xx/Kconfig#L29)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → BMA4XX 三轴加速度传感器

**配置项引用（Symbol References）**：[`CONFIG_EMUL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_EMUL)、[`CONFIG_BMA4XX`](P150_drivers_sensor_配置项参考_2.md#CONFIG_BMA4XX)、[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)。

<a id="CONFIG_EMUL_BMI160"></a>

## 153.25 `CONFIG_EMUL_BMI160`

**提示（Prompt）**：仿真 Bosch BMI160 加速度计（Accelerometer）

**说明（Help）**

这是 Bosch BMI160 加速度计（Accelerometer）的仿真器。它提供遵循简单序列的读数，使测试代码能够检查功能是否按预期工作。由于同时支持 I2C 和 SPI，它不放在 `i2c/` 或 `spi/` 目录中。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_EMUL && CONFIG_BMI160 && CONFIG_BMI160 && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/sensor/bosch/bmi160/Kconfig:219`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/bosch/bmi160/Kconfig#L219)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → Bosch BMI160 惯性测量单元（IMU）

**配置项引用（Symbol References）**：[`CONFIG_EMUL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_EMUL)、[`CONFIG_BMI160`](P151_drivers_sensor_配置项参考_3.md#CONFIG_BMI160)、[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)。

<a id="CONFIG_EMUL_BMI323"></a>

## 153.26 `CONFIG_EMUL_BMI323`

**提示（Prompt）**：BMI323 仿真器（Emulator）

**说明（Help）**

启用 BMI323 硬件仿真器（Hardware Emulator），以便在没有真实硬件时，通过仿真的 I2C 和 SPI 总线测试驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_EMUL && CONFIG_BMI323 && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/sensor/bosch/bmi323/Kconfig:42`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/bosch/bmi323/Kconfig#L42)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → BMI323 测量单元（Measurement Unit）

**配置项引用（Symbol References）**：[`CONFIG_EMUL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_EMUL)、[`CONFIG_BMI323`](P152_drivers_sensor_配置项参考_4.md#CONFIG_BMI323)、[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)。

<a id="CONFIG_EMUL_BMM350"></a>

## 153.27 `CONFIG_EMUL_BMM350`

**提示（Prompt）**：BMM350 地磁传感器（Geomagnetic Sensor）仿真器

**说明（Help）**

启用 BMM350 硬件仿真器（Hardware Emulator），以便在没有真实硬件时，通过仿真总线测试驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BMM350 && CONFIG_EMUL && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/sensor/bosch/bmm350/Kconfig:35`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/bosch/bmm350/Kconfig#L35)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → BMM350 地磁芯片（Geomagnetic Chip）

**配置项引用（Symbol References）**：[`CONFIG_BMM350`](P152_drivers_sensor_配置项参考_4.md#CONFIG_BMM350)、[`CONFIG_EMUL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_EMUL)、[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)。

<a id="CONFIG_EMUL_BMP581"></a>

## 153.28 `CONFIG_EMUL_BMP581`

**提示（Prompt）**：BMP581 大气压力传感器（Barometric Pressure Sensor）仿真器

**说明（Help）**

启用 BMP581 硬件仿真器（Hardware Emulator），以便在没有真实硬件时，通过仿真总线测试驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BMP581 && CONFIG_EMUL && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/sensor/bosch/bmp581/Kconfig:27`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/bosch/bmp581/Kconfig#L27)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers）

**配置项引用（Symbol References）**：[`CONFIG_BMP581`](P152_drivers_sensor_配置项参考_4.md#CONFIG_BMP581)、[`CONFIG_EMUL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_EMUL)、[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)。

<a id="CONFIG_EMUL_F75303"></a>

## 153.29 `CONFIG_EMUL_F75303`

**提示（Prompt）**：F75303 仿真器（Emulator）

**说明（Help）**

启用 F75303 温度传感器（Temperature Sensor）硬件仿真器。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_F75303 && CONFIG_EMUL && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/sensor/f75303/Kconfig:16`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/f75303/Kconfig#L16)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → F75303 温度传感器（Temperature Sensor）

**配置项引用（Symbol References）**：[`CONFIG_F75303`](P153_drivers_sensor_配置项参考_5.md#CONFIG_F75303)、[`CONFIG_EMUL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_EMUL)、[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)。

<a id="CONFIG_EMUL_ICM4268X"></a>

## 153.30 `CONFIG_EMUL_ICM4268X`

**提示（Prompt）**：ICM4268X 仿真器（Emulator）

**说明（Help）**

启用 ICM4268X 硬件仿真器（Hardware Emulator），以便在 `native_sim` 和 QEMU 中测试该惯性测量单元（IMU）的传感器 API。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_EMUL && CONFIG_ICM4268X && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/sensor/tdk/icm4268x/Kconfig:19`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/tdk/icm4268x/Kconfig#L19)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → ICM4268X 六轴运动跟踪器件（Six-Axis Motion Tracking Device）

**配置项引用（Symbol References）**：[`CONFIG_EMUL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_EMUL)、[`CONFIG_ICM4268X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ICM4268X)、[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)。

<a id="CONFIG_ENS160"></a>

## 153.31 `CONFIG_ENS160`

**提示（Prompt）**：ENS160 多气体传感器（Multi-gas Sensor）

**说明（Help）**

启用 ENS160 数字金属氧化物多气体传感器（Digital Metal Oxide Multi-Gas Sensor）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_SCIOSENSE_ENS160_ENABLED && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_I2C if n
CONFIG_SPI if n
```

**定义位置（Location）**：[`drivers/sensor/ens160/Kconfig:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/ens160/Kconfig#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)、[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)、[`CONFIG_SPI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SPI)。

<a id="CONFIG_ENS160_THREAD_PRIORITY"></a>

## 153.32 `CONFIG_ENS160_THREAD_PRIORITY`

**提示（Prompt）**：线程优先级（Thread Priority）

**说明（Help）**

驱动用于处理中断（Interrupt）的线程的优先级。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_ENS160_TRIGGER_OWN_THREAD && CONFIG_ENS160_TRIGGER && CONFIG_ENS160 && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
10
```

**定义位置（Location）**：[`drivers/sensor/ens160/Kconfig:41`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/ens160/Kconfig#L41)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → ENS160 多气体传感器（Multi-gas Sensor）

**配置项引用（Symbol References）**：[`CONFIG_ENS160_TRIGGER_OWN_THREAD`](P153_drivers_sensor_配置项参考_5.md#CONFIG_ENS160_TRIGGER_OWN_THREAD)、[`CONFIG_ENS160_TRIGGER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ENS160_TRIGGER)、[`CONFIG_ENS160`](P153_drivers_sensor_配置项参考_5.md#CONFIG_ENS160)、[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_ENS160_TRIGGER`。

<a id="CONFIG_ENS160_THREAD_STACK_SIZE"></a>

## 153.33 `CONFIG_ENS160_THREAD_STACK_SIZE`

**提示（Prompt）**：线程栈大小。

**说明（Help）**

驱动用于处理中断（Interrupt）的线程的栈大小（Stack Size）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_ENS160_TRIGGER_OWN_THREAD && CONFIG_ENS160_TRIGGER && CONFIG_ENS160 && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
1024
```

**定义位置（Location）**：[`drivers/sensor/ens160/Kconfig:48`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/ens160/Kconfig#L48)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → ENS160 多气体传感器（Multi-gas Sensor）

**配置项引用（Symbol References）**：[`CONFIG_ENS160_TRIGGER_OWN_THREAD`](P153_drivers_sensor_配置项参考_5.md#CONFIG_ENS160_TRIGGER_OWN_THREAD)、[`CONFIG_ENS160_TRIGGER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ENS160_TRIGGER)、[`CONFIG_ENS160`](P153_drivers_sensor_配置项参考_5.md#CONFIG_ENS160)、[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_ENS160_TRIGGER`。

<a id="CONFIG_ENS160_TRIGGER_GLOBAL_THREAD"></a>

## 153.34 `CONFIG_ENS160_TRIGGER_GLOBAL_THREAD`

**提示（Prompt）**：使用全局线程（Global Thread）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
n
```

**主动选择（Selects）**

```text
CONFIG_ENS160_TRIGGER
```

**定义位置（Location）**：[`drivers/sensor/ens160/Kconfig:24`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/ens160/Kconfig#L24)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → ENS160 多气体传感器（Multi-gas Sensor） → 触发模式（Trigger Mode）

**配置项引用（Symbol References）**：[`CONFIG_ENS160_TRIGGER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ENS160_TRIGGER)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_ENS160_TRIGGER`。

<a id="CONFIG_ENS160_TRIGGER_NONE"></a>

## 153.35 `CONFIG_ENS160_TRIGGER_NONE`

**提示（Prompt）**：不触发（No Trigger）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`drivers/sensor/ens160/Kconfig:21`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/ens160/Kconfig#L21)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → ENS160 多气体传感器（Multi-gas Sensor） → 触发模式（Trigger Mode）

<a id="CONFIG_ENS160_TRIGGER_OWN_THREAD"></a>

## 153.36 `CONFIG_ENS160_TRIGGER_OWN_THREAD`

**提示（Prompt）**：使用专用线程（Own Thread）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
n
```

**主动选择（Selects）**

```text
CONFIG_ENS160_TRIGGER
```

**定义位置（Location）**：[`drivers/sensor/ens160/Kconfig:30`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/ens160/Kconfig#L30)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → ENS160 多气体传感器（Multi-gas Sensor） → 触发模式（Trigger Mode）

**配置项引用（Symbol References）**：[`CONFIG_ENS160_TRIGGER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ENS160_TRIGGER)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_ENS160_TRIGGER`。

<a id="CONFIG_ENS210"></a>

## 153.37 `CONFIG_ENS210`

**提示（Prompt）**：ENS210 数字温湿度传感器（Digital Temperature and Humidity Sensor）

**说明（Help）**

启用 ENS210 数字温湿度传感器（Digital Temperature and Humidity Sensor）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_AMS_ENS210_ENABLED && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_I2C
CONFIG_I2C_RTIO if CONFIG_SENSOR_ASYNC_API
CONFIG_RTIO_OP_DELAY if CONFIG_SENSOR_ASYNC_API && (CONFIG_ENS210_TEMPERATURE_SINGLE || CONFIG_ENS210_HUMIDITY_SINGLE)
```

**定义位置（Location）**：[`drivers/sensor/ams/ens210/Kconfig:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/ams/ens210/Kconfig#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)、[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)、[`CONFIG_I2C_RTIO`](P106_drivers_i2c_配置项参考_2.md#CONFIG_I2C_RTIO)、[`CONFIG_SENSOR_ASYNC_API`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR_ASYNC_API)、[`CONFIG_RTIO_OP_DELAY`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_RTIO_OP_DELAY)、[`CONFIG_ENS210_TEMPERATURE_SINGLE`](P153_drivers_sensor_配置项参考_5.md#CONFIG_ENS210_TEMPERATURE_SINGLE)、[`CONFIG_ENS210_HUMIDITY_SINGLE`](P153_drivers_sensor_配置项参考_5.md#CONFIG_ENS210_HUMIDITY_SINGLE)。

<a id="CONFIG_ENS210_CRC_CHECK"></a>

## 153.38 `CONFIG_ENS210_CRC_CHECK`

**提示（Prompt）**：循环冗余校验（CRC Check）

**说明（Help）**

读取数据后检查循环冗余校验（CRC）值。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ENS210 && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/sensor/ams/ens210/Kconfig:44`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/ams/ens210/Kconfig#L44)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → ENS210 数字温湿度传感器（Digital Temperature and Humidity Sensor）

**配置项引用（Symbol References）**：[`CONFIG_ENS210`](P153_drivers_sensor_配置项参考_5.md#CONFIG_ENS210)、[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)。

<a id="CONFIG_ENS210_HUMIDITY_CONTINUOUS"></a>

## 153.39 `CONFIG_ENS210_HUMIDITY_CONTINUOUS`

**提示（Prompt）**：以连续模式（Continuous Mode）测量相对湿度

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`drivers/sensor/ams/ens210/Kconfig:40`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/ams/ens210/Kconfig#L40)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → ENS210 数字温湿度传感器（Digital Temperature and Humidity Sensor） → 湿度测量模式（Humidity Measurement Mode）

<a id="CONFIG_ENS210_HUMIDITY_OFF"></a>

## 153.40 `CONFIG_ENS210_HUMIDITY_OFF`

**提示（Prompt）**：禁用相对湿度（Relative Humidity）测量

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`drivers/sensor/ams/ens210/Kconfig:36`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/ams/ens210/Kconfig#L36)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → ENS210 数字温湿度传感器（Digital Temperature and Humidity Sensor） → 湿度测量模式（Humidity Measurement Mode）

<a id="CONFIG_ENS210_HUMIDITY_SINGLE"></a>

## 153.41 `CONFIG_ENS210_HUMIDITY_SINGLE`

**提示（Prompt）**：以单次模式（Single-shot Mode）测量相对湿度

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`drivers/sensor/ams/ens210/Kconfig:38`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/ams/ens210/Kconfig#L38)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → ENS210 数字温湿度传感器（Digital Temperature and Humidity Sensor） → 湿度测量模式（Humidity Measurement Mode）

<a id="CONFIG_ENS210_MAX_READ_RETRIES"></a>

## 153.42 `CONFIG_ENS210_MAX_READ_RETRIES`

**提示（Prompt）**：数值读取重试次数

**说明（Help）**

数值读取失败、数值无效或 CRC 校验失败时的重试次数。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_ENS210 && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
4
```

**定义位置（Location）**：[`drivers/sensor/ams/ens210/Kconfig:56`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/ams/ens210/Kconfig#L56)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → ENS210 数字温湿度传感器（Digital Temperature and Humidity Sensor）

**配置项引用（Symbol References）**：[`CONFIG_ENS210`](P153_drivers_sensor_配置项参考_5.md#CONFIG_ENS210)、[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)。

<a id="CONFIG_ENS210_MAX_STAT_RETRIES"></a>

## 153.43 `CONFIG_ENS210_MAX_STAT_RETRIES`

**提示（Prompt）**：状态读取重试次数

**说明（Help）**

状态读取失败或设备尚未就绪时的重试次数。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_ENS210 && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
4
```

**定义位置（Location）**：[`drivers/sensor/ams/ens210/Kconfig:50`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/ams/ens210/Kconfig#L50)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → ENS210 数字温湿度传感器（Digital Temperature and Humidity Sensor）

**配置项引用（Symbol References）**：[`CONFIG_ENS210`](P153_drivers_sensor_配置项参考_5.md#CONFIG_ENS210)、[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)。

<a id="CONFIG_ENS210_TEMPERATURE_CONTINUOUS"></a>

## 153.44 `CONFIG_ENS210_TEMPERATURE_CONTINUOUS`

**提示（Prompt）**：以连续模式（Continuous Mode）测量温度

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`drivers/sensor/ams/ens210/Kconfig:27`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/ams/ens210/Kconfig#L27)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → ENS210 数字温湿度传感器（Digital Temperature and Humidity Sensor） → 温度测量模式（Temperature Measurement Mode）

<a id="CONFIG_ENS210_TEMPERATURE_OFF"></a>

## 153.45 `CONFIG_ENS210_TEMPERATURE_OFF`

**提示（Prompt）**：禁用温度测量

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`drivers/sensor/ams/ens210/Kconfig:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/ams/ens210/Kconfig#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → ENS210 数字温湿度传感器（Digital Temperature and Humidity Sensor） → 温度测量模式（Temperature Measurement Mode）

<a id="CONFIG_ENS210_TEMPERATURE_SINGLE"></a>

## 153.46 `CONFIG_ENS210_TEMPERATURE_SINGLE`

**提示（Prompt）**：以单次模式（Single-shot Mode）测量温度

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`drivers/sensor/ams/ens210/Kconfig:25`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/ams/ens210/Kconfig#L25)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → ENS210 数字温湿度传感器（Digital Temperature and Humidity Sensor） → 温度测量模式（Temperature Measurement Mode）

<a id="CONFIG_EQDC_MCUX"></a>

## 153.47 `CONFIG_EQDC_MCUX`

**提示（Prompt）**：NXP eQDC 驱动

**说明（Help）**

启用 NXP eQDC 驱动。EQDC 的相位输入通过通用多路复用器子系统（Generic Mux Subsystem），经片上 INPUTMUX 路由。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NXP_MCUX_EQDC_ENABLED && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_MUX
CONFIG_PINCTRL
```

**定义位置（Location）**：[`drivers/sensor/nxp/eqdc_mcux/Kconfig:5`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/nxp/eqdc_mcux/Kconfig#L5)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)、[`CONFIG_MUX`](P130_drivers_mux_配置项参考.md#CONFIG_MUX)、[`CONFIG_PINCTRL`](P136_drivers_pinctrl_配置项参考.md#CONFIG_PINCTRL)。

<a id="CONFIG_EQDC_MCUX_TRIGGER"></a>

## 153.48 `CONFIG_EQDC_MCUX_TRIGGER`

**提示（Prompt）**：EQDC 触发支持（Trigger Support）

**说明（Help）**

启用 EQDC 触发支持，使驱动能够在位置值上溢／下溢（Roll-over/under）等事件发生时产生中断。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_EQDC_MCUX && CONFIG_SENSOR
```

**定义位置（Location）**：[`drivers/sensor/nxp/eqdc_mcux/Kconfig:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/nxp/eqdc_mcux/Kconfig#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → NXP eQDC 驱动

**配置项引用（Symbol References）**：[`CONFIG_EQDC_MCUX`](P153_drivers_sensor_配置项参考_5.md#CONFIG_EQDC_MCUX)、[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)。

<a id="CONFIG_ESP32_TEMP"></a>

## 153.49 `CONFIG_ESP32_TEMP`

**提示（Prompt）**：ESP32 温度传感器（Temperature Sensor）

**说明（Help）**

启用特定 ESP 目标平台上的温度传感器（Temperature Sensor）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ESPRESSIF_ESP32_TEMP_ENABLED && !CONFIG_SOC_SERIES_ESP32 && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/sensor/espressif/esp32_temp/Kconfig:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/espressif/esp32_temp/Kconfig#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_ESP32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32)、[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)。

<a id="CONFIG_EVERLIGHT_ALS_PT19"></a>

## 153.50 `CONFIG_EVERLIGHT_ALS_PT19`

**提示（Prompt）**：Everlight ALS-PT19 环境光传感器（Ambient Light Sensor）

**说明（Help）**

启用 Everlight ALS-PT19 环境光传感器（Ambient Light Sensor）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_EVERLIGHT_ALS_PT19_ENABLED && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_ADC
```

**定义位置（Location）**：[`drivers/sensor/everlight/als_pt19/Kconfig:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/everlight/als_pt19/Kconfig#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)、[`CONFIG_ADC`](P047_drivers_adc_配置项参考_1.md#CONFIG_ADC)。

<a id="CONFIG_EXPLORIR_M"></a>

## 153.51 `CONFIG_EXPLORIR_M`

**提示（Prompt）**：ExplorIR-M 二氧化碳传感器（CO2 Sensor）

**说明（Help）**

启用 ExplorIR-M 二氧化碳传感器（CO2 Sensor）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_GSS_EXPLORIR_M_ENABLED && CONFIG_UART_INTERRUPT_DRIVEN && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/sensor/explorir_m/Kconfig:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/explorir_m/Kconfig#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers）

**配置项引用（Symbol References）**：[`CONFIG_UART_INTERRUPT_DRIVEN`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_INTERRUPT_DRIVEN)、[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)。

<a id="CONFIG_F75303"></a>

## 153.52 `CONFIG_F75303`

**提示（Prompt）**：F75303 温度传感器（Temperature Sensor）

**说明（Help）**

启用 Fintek F75303 温度传感器（Temperature Sensor）驱动。此器件具有三个温度通道：一个本地（片上）通道和两个远程通道。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_FINTEK_F75303_ENABLED && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_I2C
```

**定义位置（Location）**：[`drivers/sensor/f75303/Kconfig:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/f75303/Kconfig#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)、[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)。

<a id="CONFIG_FCX_MLDX5"></a>

## 153.53 `CONFIG_FCX_MLDX5`

**提示（Prompt）**：FCX-MLDx5 氧气传感器（O2 Sensor）

**说明（Help）**

启用 FCX-MLD25 或 FCX-MLD95 氧气传感器（O2 Sensor）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_AP_FCX_MLDX5_ENABLED && CONFIG_UART_INTERRUPT_DRIVEN && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/sensor/fcx_mldx5/Kconfig:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/fcx_mldx5/Kconfig#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers）

**配置项引用（Symbol References）**：[`CONFIG_UART_INTERRUPT_DRIVEN`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_INTERRUPT_DRIVEN)、[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)。

<a id="CONFIG_FDC1004"></a>

## 153.54 `CONFIG_FDC1004`

**提示（Prompt）**：Texas Instruments FDC1004 电容数字转换器（Capacitance-to-Digital Converter）

**说明（Help）**

启用 TI FDC1004 四通道、16 位电容数字转换器（Capacitance-to-Digital Converter）驱动。该器件通过 I2C 通信，使用 `<fdc1004.h>` 中定义的私有通道 ID，通过 Zephyr 传感器 API 提供四个单端测量通道（Single-ended Measurement Channel），即 CIN1 至 CIN4。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_TI_FDC1004_ENABLED && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_I2C
```

**定义位置（Location）**：[`drivers/sensor/ti/fdc1004/Kconfig:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/ti/fdc1004/Kconfig#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)、[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)。

<a id="CONFIG_FDC2X1X"></a>

## 153.55 `CONFIG_FDC2X1X`

**提示（Prompt）**：FDC2X1X 电容数字转换器（Capacitance-to-Digital Converter）

**说明（Help）**

启用 FDC2X1X 电容数字转换器（Capacitance-to-Digital Converter）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_TI_FDC2X1X_ENABLED && (CONFIG_FULL_LIBC_SUPPORTED || CONFIG_EXTERNAL_LIBC) && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_I2C
```

**定义位置（Location）**：[`drivers/sensor/ti/fdc2x1x/Kconfig:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/ti/fdc2x1x/Kconfig#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers）

**配置项引用（Symbol References）**：[`CONFIG_FULL_LIBC_SUPPORTED`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_FULL_LIBC_SUPPORTED)、[`CONFIG_EXTERNAL_LIBC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_EXTERNAL_LIBC)、[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)、[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)。

<a id="CONFIG_FDC2X1X_THREAD_PRIORITY"></a>

## 153.56 `CONFIG_FDC2X1X_THREAD_PRIORITY`

**提示（Prompt）**：线程优先级（Thread Priority）

**说明（Help）**

驱动用于处理中断（Interrupt）的线程的优先级。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_FDC2X1X_TRIGGER_OWN_THREAD && CONFIG_FDC2X1X_TRIGGER && CONFIG_FDC2X1X && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
10
```

**定义位置（Location）**：[`drivers/sensor/ti/fdc2x1x/Kconfig:43`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/ti/fdc2x1x/Kconfig#L43)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → FDC2X1X 电容数字转换器（Capacitance-to-Digital Converter）

**配置项引用（Symbol References）**：[`CONFIG_FDC2X1X_TRIGGER_OWN_THREAD`](P153_drivers_sensor_配置项参考_5.md#CONFIG_FDC2X1X_TRIGGER_OWN_THREAD)、[`CONFIG_FDC2X1X_TRIGGER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_FDC2X1X_TRIGGER)、[`CONFIG_FDC2X1X`](P153_drivers_sensor_配置项参考_5.md#CONFIG_FDC2X1X)、[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_FDC2X1X_TRIGGER`。

<a id="CONFIG_FDC2X1X_THREAD_STACK_SIZE"></a>

## 153.57 `CONFIG_FDC2X1X_THREAD_STACK_SIZE`

**提示（Prompt）**：线程栈大小。

**说明（Help）**

驱动用于处理中断（Interrupt）的线程的栈大小（Stack Size）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_FDC2X1X_TRIGGER_OWN_THREAD && CONFIG_FDC2X1X_TRIGGER && CONFIG_FDC2X1X && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
1024
```

**定义位置（Location）**：[`drivers/sensor/ti/fdc2x1x/Kconfig:50`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/ti/fdc2x1x/Kconfig#L50)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → FDC2X1X 电容数字转换器（Capacitance-to-Digital Converter）

**配置项引用（Symbol References）**：[`CONFIG_FDC2X1X_TRIGGER_OWN_THREAD`](P153_drivers_sensor_配置项参考_5.md#CONFIG_FDC2X1X_TRIGGER_OWN_THREAD)、[`CONFIG_FDC2X1X_TRIGGER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_FDC2X1X_TRIGGER)、[`CONFIG_FDC2X1X`](P153_drivers_sensor_配置项参考_5.md#CONFIG_FDC2X1X)、[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_FDC2X1X_TRIGGER`。

<a id="CONFIG_FDC2X1X_TRIGGER_GLOBAL_THREAD"></a>

## 153.58 `CONFIG_FDC2X1X_TRIGGER_GLOBAL_THREAD`

**提示（Prompt）**：使用全局线程（Global Thread）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
n
```

**主动选择（Selects）**

```text
CONFIG_FDC2X1X_TRIGGER
```

**定义位置（Location）**：[`drivers/sensor/ti/fdc2x1x/Kconfig:26`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/ti/fdc2x1x/Kconfig#L26)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → FDC2X1X 电容数字转换器（Capacitance-to-Digital Converter） → 触发模式（Trigger Mode）

**配置项引用（Symbol References）**：[`CONFIG_FDC2X1X_TRIGGER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_FDC2X1X_TRIGGER)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_FDC2X1X_TRIGGER`。

<a id="CONFIG_FDC2X1X_TRIGGER_NONE"></a>

## 153.59 `CONFIG_FDC2X1X_TRIGGER_NONE`

**提示（Prompt）**：不触发（No Trigger）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`drivers/sensor/ti/fdc2x1x/Kconfig:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/ti/fdc2x1x/Kconfig#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → FDC2X1X 电容数字转换器（Capacitance-to-Digital Converter） → 触发模式（Trigger Mode）

<a id="CONFIG_FDC2X1X_TRIGGER_OWN_THREAD"></a>

## 153.60 `CONFIG_FDC2X1X_TRIGGER_OWN_THREAD`

**提示（Prompt）**：使用专用线程（Own Thread）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
n
```

**主动选择（Selects）**

```text
CONFIG_FDC2X1X_TRIGGER
```

**定义位置（Location）**：[`drivers/sensor/ti/fdc2x1x/Kconfig:32`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/ti/fdc2x1x/Kconfig#L32)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → FDC2X1X 电容数字转换器（Capacitance-to-Digital Converter） → 触发模式（Trigger Mode）

**配置项引用（Symbol References）**：[`CONFIG_FDC2X1X_TRIGGER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_FDC2X1X_TRIGGER)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_FDC2X1X_TRIGGER`。

<a id="CONFIG_FLOW_METER"></a>

## 153.61 `CONFIG_FLOW_METER`

**提示（Prompt）**：霍尔效应流量计（Hall-effect Flow Meter）驱动

**说明（Help）**

启用采用霍尔效应、输出脉冲的流量计（Hall-effect Pulse-output Flow Meter）驱动，提供流量（Flow Rate）和累计体积（Cumulative Volume）通道。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ZEPHYR_FLOW_METER_ENABLED && CONFIG_GPIO && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/sensor/flow_meter/Kconfig:5`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/flow_meter/Kconfig#L5)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers）

**配置项引用（Symbol References）**：[`CONFIG_GPIO`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO)、[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)。

<a id="CONFIG_FXAS21002"></a>

## 153.62 `CONFIG_FXAS21002`

**提示（Prompt）**：FXAS21002 陀螺仪（Gyroscope）驱动

**说明（Help）**

启用 FXAS21002 陀螺仪（Gyroscope）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NXP_FXAS21002_ENABLED && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_I2C if n
CONFIG_SPI if n
```

**定义位置（Location）**：[`drivers/sensor/nxp/fxas21002/Kconfig:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/nxp/fxas21002/Kconfig#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)、[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)、[`CONFIG_SPI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SPI)。

<a id="CONFIG_FXAS21002_DR"></a>

## 153.63 `CONFIG_FXAS21002_DR`

**提示（Prompt）**：输出数据速率（Output Data Rate，ODR）

**说明（Help）**

选择输出数据速率（Output Data Rate）：

- 0：800 Hz。
- 1：400 Hz。
- 2：200 Hz。
- 3：100 Hz。
- 4：50 Hz。
- 5：25 Hz。
- 6：12.5 Hz。
- 7：12.5 Hz。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_FXAS21002 && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
3
```

**取值范围（Ranges）**

```text
[0, 7]
```

**定义位置（Location）**：[`drivers/sensor/nxp/fxas21002/Kconfig:37`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/nxp/fxas21002/Kconfig#L37)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → FXAS21002 陀螺仪（Gyroscope）驱动

**配置项引用（Symbol References）**：[`CONFIG_FXAS21002`](P153_drivers_sensor_配置项参考_5.md#CONFIG_FXAS21002)、[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)。

<a id="CONFIG_FXAS21002_DRDY_INT1"></a>

## 153.64 `CONFIG_FXAS21002_DRDY_INT1`

**提示（Prompt）**：将数据就绪中断（Data Ready Interrupt）路由至 INT1 引脚

**说明（Help）**

选择 Y 将数据就绪中断（Data Ready Interrupt）路由至 INT1 引脚；选择 N 将其路由至 INT2 引脚。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_FXAS21002_TRIGGER && CONFIG_FXAS21002 && CONFIG_SENSOR
```

**定义位置（Location）**：[`drivers/sensor/nxp/fxas21002/Kconfig:77`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/nxp/fxas21002/Kconfig#L77)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → FXAS21002 陀螺仪（Gyroscope）驱动

**配置项引用（Symbol References）**：[`CONFIG_FXAS21002_TRIGGER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_FXAS21002_TRIGGER)、[`CONFIG_FXAS21002`](P153_drivers_sensor_配置项参考_5.md#CONFIG_FXAS21002)、[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_FXAS21002_TRIGGER`。

<a id="CONFIG_FXAS21002_RANGE"></a>

## 153.65 `CONFIG_FXAS21002_RANGE`

**提示（Prompt）**：满量程范围（Full Scale Range）

**说明（Help）**

选择满量程范围（Full Scale Range）：

- 0：±2000 dps（62.5 mdps/LSB）。
- 1：±1000 dps（31.25 mdps/LSB）。
- 2：±500 dps（15.625 mdps/LSB）。
- 3：±250 dps（7.8125 mdps/LSB）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_FXAS21002 && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
0
```

**取值范围（Ranges）**

```text
[0, 3]
```

**定义位置（Location）**：[`drivers/sensor/nxp/fxas21002/Kconfig:26`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/nxp/fxas21002/Kconfig#L26)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → FXAS21002 陀螺仪（Gyroscope）驱动

**配置项引用（Symbol References）**：[`CONFIG_FXAS21002`](P153_drivers_sensor_配置项参考_5.md#CONFIG_FXAS21002)、[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)。

<a id="CONFIG_FXAS21002_THREAD_PRIORITY"></a>

## 153.66 `CONFIG_FXAS21002_THREAD_PRIORITY`

**提示（Prompt）**：专用线程优先级（Own Thread Priority）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_FXAS21002_TRIGGER_OWN_THREAD && CONFIG_FXAS21002_TRIGGER && CONFIG_FXAS21002 && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
10
```

**定义位置（Location）**：[`drivers/sensor/nxp/fxas21002/Kconfig:83`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/nxp/fxas21002/Kconfig#L83)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → FXAS21002 陀螺仪（Gyroscope）驱动

**配置项引用（Symbol References）**：[`CONFIG_FXAS21002_TRIGGER_OWN_THREAD`](P153_drivers_sensor_配置项参考_5.md#CONFIG_FXAS21002_TRIGGER_OWN_THREAD)、[`CONFIG_FXAS21002_TRIGGER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_FXAS21002_TRIGGER)、[`CONFIG_FXAS21002`](P153_drivers_sensor_配置项参考_5.md#CONFIG_FXAS21002)、[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_FXAS21002_TRIGGER`。

<a id="CONFIG_FXAS21002_THREAD_STACK_SIZE"></a>

## 153.67 `CONFIG_FXAS21002_THREAD_STACK_SIZE`

**提示（Prompt）**：专用线程栈大小（Own Thread Stack Size）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_FXAS21002_TRIGGER_OWN_THREAD && CONFIG_FXAS21002_TRIGGER && CONFIG_FXAS21002 && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
1024
```

**定义位置（Location）**：[`drivers/sensor/nxp/fxas21002/Kconfig:88`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/nxp/fxas21002/Kconfig#L88)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → FXAS21002 陀螺仪（Gyroscope）驱动

**配置项引用（Symbol References）**：[`CONFIG_FXAS21002_TRIGGER_OWN_THREAD`](P153_drivers_sensor_配置项参考_5.md#CONFIG_FXAS21002_TRIGGER_OWN_THREAD)、[`CONFIG_FXAS21002_TRIGGER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_FXAS21002_TRIGGER)、[`CONFIG_FXAS21002`](P153_drivers_sensor_配置项参考_5.md#CONFIG_FXAS21002)、[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_FXAS21002_TRIGGER`。

<a id="CONFIG_FXAS21002_TRIGGER_GLOBAL_THREAD"></a>

## 153.68 `CONFIG_FXAS21002_TRIGGER_GLOBAL_THREAD`

**提示（Prompt）**：使用全局线程（Global Thread）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_GPIO && (n || n) && <choice>
```

**主动选择（Selects）**

```text
CONFIG_FXAS21002_TRIGGER
```

**定义位置（Location）**：[`drivers/sensor/nxp/fxas21002/Kconfig:59`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/nxp/fxas21002/Kconfig#L59)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → FXAS21002 陀螺仪（Gyroscope）驱动 → 触发模式（Trigger Mode）

**配置项引用（Symbol References）**：[`CONFIG_GPIO`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO)、[`CONFIG_FXAS21002_TRIGGER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_FXAS21002_TRIGGER)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_FXAS21002_TRIGGER`。

<a id="CONFIG_FXAS21002_TRIGGER_NONE"></a>

## 153.69 `CONFIG_FXAS21002_TRIGGER_NONE`

**提示（Prompt）**：不触发（No Trigger）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`drivers/sensor/nxp/fxas21002/Kconfig:56`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/nxp/fxas21002/Kconfig#L56)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → FXAS21002 陀螺仪（Gyroscope）驱动 → 触发模式（Trigger Mode）

<a id="CONFIG_FXAS21002_TRIGGER_OWN_THREAD"></a>

## 153.70 `CONFIG_FXAS21002_TRIGGER_OWN_THREAD`

**提示（Prompt）**：使用专用线程（Own Thread）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**主动选择（Selects）**

```text
CONFIG_FXAS21002_TRIGGER
```

**定义位置（Location）**：[`drivers/sensor/nxp/fxas21002/Kconfig:66`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/nxp/fxas21002/Kconfig#L66)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → FXAS21002 陀螺仪（Gyroscope）驱动 → 触发模式（Trigger Mode）

**配置项引用（Symbol References）**：[`CONFIG_FXAS21002_TRIGGER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_FXAS21002_TRIGGER)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_FXAS21002_TRIGGER`。

<a id="CONFIG_FXAS21002_WHOAMI"></a>

## 153.71 `CONFIG_FXAS21002_WHOAMI`

**提示（Prompt）**：WHOAMI 值

**说明（Help）**

数据手册规定了 WHOAMI 寄存器的值，但部分量产前器件可能使用不同的值。通常无需修改此配置选项的默认值。

**类型（Type）**：十六进制整数（Hexadecimal），`hex`。

**依赖条件（Dependencies）**

```text
CONFIG_FXAS21002 && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
0xd7
```

**取值范围（Ranges）**

```text
[0x00, 0xff]
```

**定义位置（Location）**：[`drivers/sensor/nxp/fxas21002/Kconfig:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/nxp/fxas21002/Kconfig#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → FXAS21002 陀螺仪（Gyroscope）驱动

**配置项引用（Symbol References）**：[`CONFIG_FXAS21002`](P153_drivers_sensor_配置项参考_5.md#CONFIG_FXAS21002)、[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)。

<a id="CONFIG_FXLS8974"></a>

## 153.72 `CONFIG_FXLS8974`

**提示（Prompt）**：FXLS8974 加速度计（Accelerometer）驱动

**说明（Help）**

启用 FXLS8974 加速度计（Accelerometer）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NXP_FXLS8974_ENABLED && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_I2C if n
CONFIG_SPI if n
```

**定义位置（Location）**：[`drivers/sensor/nxp/fxls8974/Kconfig:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/nxp/fxls8974/Kconfig#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)、[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)、[`CONFIG_SPI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SPI)。

<a id="CONFIG_FXLS8974_DRDY_INT1"></a>

## 153.73 `CONFIG_FXLS8974_DRDY_INT1`

**提示（Prompt）**：将数据就绪中断（Data Ready Interrupt）路由至 INT1 引脚

**说明（Help）**

选择 Y 将数据就绪中断（Data Ready Interrupt）路由至 INT1 引脚；选择 N 将其路由至 INT2 引脚。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_FXLS8974_TRIGGER && CONFIG_FXLS8974 && CONFIG_SENSOR
```

**定义位置（Location）**：[`drivers/sensor/nxp/fxls8974/Kconfig:40`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/nxp/fxls8974/Kconfig#L40)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → FXLS8974 加速度计（Accelerometer）驱动

**配置项引用（Symbol References）**：[`CONFIG_FXLS8974_TRIGGER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_FXLS8974_TRIGGER)、[`CONFIG_FXLS8974`](P153_drivers_sensor_配置项参考_5.md#CONFIG_FXLS8974)、[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_FXLS8974_TRIGGER`。

<a id="CONFIG_FXLS8974_THREAD_PRIORITY"></a>

## 153.74 `CONFIG_FXLS8974_THREAD_PRIORITY`

**提示（Prompt）**：专用线程优先级（Own Thread Priority）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_FXLS8974_TRIGGER_OWN_THREAD && CONFIG_FXLS8974_TRIGGER && CONFIG_FXLS8974 && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
10
```

**定义位置（Location）**：[`drivers/sensor/nxp/fxls8974/Kconfig:49`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/nxp/fxls8974/Kconfig#L49)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → FXLS8974 加速度计（Accelerometer）驱动

**配置项引用（Symbol References）**：[`CONFIG_FXLS8974_TRIGGER_OWN_THREAD`](P153_drivers_sensor_配置项参考_5.md#CONFIG_FXLS8974_TRIGGER_OWN_THREAD)、[`CONFIG_FXLS8974_TRIGGER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_FXLS8974_TRIGGER)、[`CONFIG_FXLS8974`](P153_drivers_sensor_配置项参考_5.md#CONFIG_FXLS8974)、[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_FXLS8974_TRIGGER`。

<a id="CONFIG_FXLS8974_THREAD_STACK_SIZE"></a>

## 153.75 `CONFIG_FXLS8974_THREAD_STACK_SIZE`

**提示（Prompt）**：专用线程栈大小（Own Thread Stack Size）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_FXLS8974_TRIGGER_OWN_THREAD && CONFIG_FXLS8974_TRIGGER && CONFIG_FXLS8974 && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
1024
```

**定义位置（Location）**：[`drivers/sensor/nxp/fxls8974/Kconfig:54`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/nxp/fxls8974/Kconfig#L54)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → FXLS8974 加速度计（Accelerometer）驱动

**配置项引用（Symbol References）**：[`CONFIG_FXLS8974_TRIGGER_OWN_THREAD`](P153_drivers_sensor_配置项参考_5.md#CONFIG_FXLS8974_TRIGGER_OWN_THREAD)、[`CONFIG_FXLS8974_TRIGGER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_FXLS8974_TRIGGER)、[`CONFIG_FXLS8974`](P153_drivers_sensor_配置项参考_5.md#CONFIG_FXLS8974)、[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_FXLS8974_TRIGGER`。

<a id="CONFIG_FXLS8974_TRIGGER_GLOBAL_THREAD"></a>

## 153.76 `CONFIG_FXLS8974_TRIGGER_GLOBAL_THREAD`

**提示（Prompt）**：使用全局线程（Global Thread）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_GPIO && (n || n) && <choice>
```

**主动选择（Selects）**

```text
CONFIG_FXLS8974_TRIGGER
```

**定义位置（Location）**：[`drivers/sensor/nxp/fxls8974/Kconfig:24`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/nxp/fxls8974/Kconfig#L24)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → FXLS8974 加速度计（Accelerometer）驱动 → 触发模式（Trigger Mode）

**配置项引用（Symbol References）**：[`CONFIG_GPIO`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO)、[`CONFIG_FXLS8974_TRIGGER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_FXLS8974_TRIGGER)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_FXLS8974_TRIGGER`。

<a id="CONFIG_FXLS8974_TRIGGER_NONE"></a>

## 153.77 `CONFIG_FXLS8974_TRIGGER_NONE`

**提示（Prompt）**：不触发（No Trigger）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`drivers/sensor/nxp/fxls8974/Kconfig:21`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/nxp/fxls8974/Kconfig#L21)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → FXLS8974 加速度计（Accelerometer）驱动 → 触发模式（Trigger Mode）

<a id="CONFIG_FXLS8974_TRIGGER_OWN_THREAD"></a>

## 153.78 `CONFIG_FXLS8974_TRIGGER_OWN_THREAD`

**提示（Prompt）**：使用专用线程（Own Thread）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**主动选择（Selects）**

```text
CONFIG_FXLS8974_TRIGGER
```

**定义位置（Location）**：[`drivers/sensor/nxp/fxls8974/Kconfig:31`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/nxp/fxls8974/Kconfig#L31)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → FXLS8974 加速度计（Accelerometer）驱动 → 触发模式（Trigger Mode）

**配置项引用（Symbol References）**：[`CONFIG_FXLS8974_TRIGGER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_FXLS8974_TRIGGER)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_FXLS8974_TRIGGER`。

<a id="CONFIG_FXOS8700"></a>

## 153.79 `CONFIG_FXOS8700`

**提示（Prompt）**：FXOS8700 加速度计／磁力计（Accelerometer/Magnetometer）驱动

**说明（Help）**

启用 FXOS8700 加速度计／磁力计（Accelerometer/Magnetometer）驱动。此驱动也支持 MMA8451Q、MMA8652FC 和 MMA8653FC 加速度计。用于这些加速度计之一时，应选择仅加速度计模式（Accelerometer-only Mode）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NXP_FXOS8700_ENABLED && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_I2C if n
CONFIG_SPI if n
```

**定义位置（Location）**：[`drivers/sensor/nxp/fxos8700/Kconfig:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/nxp/fxos8700/Kconfig#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)、[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)、[`CONFIG_SPI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SPI)。

<a id="CONFIG_FXOS8700_DRDY_INT1"></a>

## 153.80 `CONFIG_FXOS8700_DRDY_INT1`

**提示（Prompt）**：将数据就绪中断（Data Ready Interrupt）路由至 INT1 引脚

**说明（Help）**

选择 Y 将数据就绪中断（Data Ready Interrupt）路由至 INT1 引脚；选择 N 将其路由至 INT2 引脚。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_FXOS8700_TRIGGER && CONFIG_FXOS8700 && CONFIG_SENSOR
```

**定义位置（Location）**：[`drivers/sensor/nxp/fxos8700/Kconfig:66`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/nxp/fxos8700/Kconfig#L66)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → FXOS8700 加速度计／磁力计（Accelerometer/Magnetometer）驱动

**配置项引用（Symbol References）**：[`CONFIG_FXOS8700_TRIGGER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_FXOS8700_TRIGGER)、[`CONFIG_FXOS8700`](P153_drivers_sensor_配置项参考_5.md#CONFIG_FXOS8700)、[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_FXOS8700_TRIGGER`。

<a id="CONFIG_FXOS8700_MAG_VECM"></a>

## 153.81 `CONFIG_FXOS8700_MAG_VECM`

**提示（Prompt）**：磁矢量模值检测（Magnetic Vector-magnitude Detection）

**说明（Help）**

启用磁矢量模值检测（Magnetic Vector-magnitude Detection）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_FXOS8700_TRIGGER && CONFIG_FXOS8700 && CONFIG_SENSOR
```

**定义位置（Location）**：[`drivers/sensor/nxp/fxos8700/Kconfig:110`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/nxp/fxos8700/Kconfig#L110)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → FXOS8700 加速度计／磁力计（Accelerometer/Magnetometer）驱动

**配置项引用（Symbol References）**：[`CONFIG_FXOS8700_TRIGGER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_FXOS8700_TRIGGER)、[`CONFIG_FXOS8700`](P153_drivers_sensor_配置项参考_5.md#CONFIG_FXOS8700)、[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_FXOS8700_TRIGGER`。

<a id="CONFIG_FXOS8700_MAG_VECM_INT1"></a>

## 153.82 `CONFIG_FXOS8700_MAG_VECM_INT1`

**提示（Prompt）**：将磁矢量模值中断路由至 INT1 引脚

**说明（Help）**

选择 Y 将磁矢量模值中断（Magnetic Vector-magnitude Interrupt）路由至 INT1 引脚；选择 N 将其路由至 INT2 引脚。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_FXOS8700_MAG_VECM && CONFIG_FXOS8700_TRIGGER && CONFIG_FXOS8700 && CONFIG_SENSOR
```

**定义位置（Location）**：[`drivers/sensor/nxp/fxos8700/Kconfig:117`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/nxp/fxos8700/Kconfig#L117)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → FXOS8700 加速度计／磁力计（Accelerometer/Magnetometer）驱动 → 磁矢量模值检测（Magnetic Vector-magnitude Detection）

**配置项引用（Symbol References）**：[`CONFIG_FXOS8700_MAG_VECM`](P153_drivers_sensor_配置项参考_5.md#CONFIG_FXOS8700_MAG_VECM)、[`CONFIG_FXOS8700_TRIGGER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_FXOS8700_TRIGGER)、[`CONFIG_FXOS8700`](P153_drivers_sensor_配置项参考_5.md#CONFIG_FXOS8700)、[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_FXOS8700_TRIGGER`。

<a id="CONFIG_FXOS8700_MODE"></a>

## 153.83 `CONFIG_FXOS8700_MODE`

**提示（Prompt）**：模式（Mode）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_FXOS8700 && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
CONFIG_FXOS8700_MODE_HYBRID
```

**可选项（Choices）**

```text
CONFIG_FXOS8700_MODE_ACCEL
CONFIG_FXOS8700_MODE_MAGN
CONFIG_FXOS8700_MODE_HYBRID
```

**定义位置（Location）**：[`drivers/sensor/nxp/fxos8700/Kconfig:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/nxp/fxos8700/Kconfig#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → FXOS8700 加速度计／磁力计（Accelerometer/Magnetometer）驱动

**配置项引用（Symbol References）**：[`CONFIG_FXOS8700`](P153_drivers_sensor_配置项参考_5.md#CONFIG_FXOS8700)、[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)、[`CONFIG_FXOS8700_MODE_HYBRID`](P153_drivers_sensor_配置项参考_5.md#CONFIG_FXOS8700_MODE_HYBRID)、[`CONFIG_FXOS8700_MODE_ACCEL`](P153_drivers_sensor_配置项参考_5.md#CONFIG_FXOS8700_MODE_ACCEL)、[`CONFIG_FXOS8700_MODE_MAGN`](P153_drivers_sensor_配置项参考_5.md#CONFIG_FXOS8700_MODE_MAGN)。

<a id="CONFIG_FXOS8700_MODE_ACCEL"></a>

## 153.84 `CONFIG_FXOS8700_MODE_ACCEL`

**提示（Prompt）**：仅加速度计模式（Accelerometer-only Mode）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_FXOS8700_MODE>
```

**定义位置（Location）**：[`drivers/sensor/nxp/fxos8700/Kconfig:24`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/nxp/fxos8700/Kconfig#L24)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → FXOS8700 加速度计／磁力计（Accelerometer/Magnetometer）驱动 → 模式（Mode）

**配置项引用（Symbol References）**：[`CONFIG_FXOS8700_MODE`](P153_drivers_sensor_配置项参考_5.md#CONFIG_FXOS8700_MODE)。

<a id="CONFIG_FXOS8700_MODE_HYBRID"></a>

## 153.85 `CONFIG_FXOS8700_MODE_HYBRID`

**提示（Prompt）**：混合模式（Hybrid Mode，加速度计＋磁力计）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_FXOS8700_MODE>
```

**定义位置（Location）**：[`drivers/sensor/nxp/fxos8700/Kconfig:30`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/nxp/fxos8700/Kconfig#L30)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → FXOS8700 加速度计／磁力计（Accelerometer/Magnetometer）驱动 → 模式（Mode）

**配置项引用（Symbol References）**：[`CONFIG_FXOS8700_MODE`](P153_drivers_sensor_配置项参考_5.md#CONFIG_FXOS8700_MODE)。

<a id="CONFIG_FXOS8700_MODE_MAGN"></a>

## 153.86 `CONFIG_FXOS8700_MODE_MAGN`

**提示（Prompt）**：仅磁力计模式（Magnetometer-only Mode）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_FXOS8700_MODE>
```

**定义位置（Location）**：[`drivers/sensor/nxp/fxos8700/Kconfig:27`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/nxp/fxos8700/Kconfig#L27)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → FXOS8700 加速度计／磁力计（Accelerometer/Magnetometer）驱动 → 模式（Mode）

**配置项引用（Symbol References）**：[`CONFIG_FXOS8700_MODE`](P153_drivers_sensor_配置项参考_5.md#CONFIG_FXOS8700_MODE)。

<a id="CONFIG_FXOS8700_MOTION"></a>

## 153.87 `CONFIG_FXOS8700_MOTION`

**提示（Prompt）**：运动检测（Motion Detection）

**说明（Help）**

启用运动检测（Motion Detection）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_FXOS8700_TRIGGER && CONFIG_FXOS8700 && CONFIG_SENSOR
```

**定义位置（Location）**：[`drivers/sensor/nxp/fxos8700/Kconfig:99`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/nxp/fxos8700/Kconfig#L99)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → FXOS8700 加速度计／磁力计（Accelerometer/Magnetometer）驱动

**配置项引用（Symbol References）**：[`CONFIG_FXOS8700_TRIGGER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_FXOS8700_TRIGGER)、[`CONFIG_FXOS8700`](P153_drivers_sensor_配置项参考_5.md#CONFIG_FXOS8700)、[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_FXOS8700_TRIGGER`。

<a id="CONFIG_FXOS8700_MOTION_INT1"></a>

## 153.88 `CONFIG_FXOS8700_MOTION_INT1`

**提示（Prompt）**：将运动中断（Motion Interrupt）路由至 INT1 引脚

**说明（Help）**

选择 Y 将运动中断（Motion Interrupt）路由至 INT1 引脚；选择 N 将其路由至 INT2 引脚。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_FXOS8700_MOTION && CONFIG_FXOS8700_TRIGGER && CONFIG_FXOS8700 && CONFIG_SENSOR
```

**定义位置（Location）**：[`drivers/sensor/nxp/fxos8700/Kconfig:104`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/nxp/fxos8700/Kconfig#L104)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → FXOS8700 加速度计／磁力计（Accelerometer/Magnetometer）驱动 → 运动检测（Motion Detection）

**配置项引用（Symbol References）**：[`CONFIG_FXOS8700_MOTION`](P153_drivers_sensor_配置项参考_5.md#CONFIG_FXOS8700_MOTION)、[`CONFIG_FXOS8700_TRIGGER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_FXOS8700_TRIGGER)、[`CONFIG_FXOS8700`](P153_drivers_sensor_配置项参考_5.md#CONFIG_FXOS8700)、[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_FXOS8700_TRIGGER`。

<a id="CONFIG_FXOS8700_PULSE"></a>

## 153.89 `CONFIG_FXOS8700_PULSE`

**提示（Prompt）**：脉冲检测（Pulse Detection）

**说明（Help）**

启用脉冲检测（Pulse Detection）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_FXOS8700_TRIGGER && CONFIG_FXOS8700 && CONFIG_SENSOR
```

**定义位置（Location）**：[`drivers/sensor/nxp/fxos8700/Kconfig:85`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/nxp/fxos8700/Kconfig#L85)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → FXOS8700 加速度计／磁力计（Accelerometer/Magnetometer）驱动

**配置项引用（Symbol References）**：[`CONFIG_FXOS8700_TRIGGER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_FXOS8700_TRIGGER)、[`CONFIG_FXOS8700`](P153_drivers_sensor_配置项参考_5.md#CONFIG_FXOS8700)、[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_FXOS8700_TRIGGER`。

<a id="CONFIG_FXOS8700_PULSE_INT1"></a>

## 153.90 `CONFIG_FXOS8700_PULSE_INT1`

**提示（Prompt）**：将脉冲中断（Pulse Interrupt）路由至 INT1 引脚

**说明（Help）**

选择 Y 将脉冲中断（Pulse Interrupt）路由至 INT1 引脚；选择 N 将其路由至 INT2 引脚。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_FXOS8700_PULSE && CONFIG_FXOS8700_TRIGGER && CONFIG_FXOS8700 && CONFIG_SENSOR
```

**定义位置（Location）**：[`drivers/sensor/nxp/fxos8700/Kconfig:92`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/nxp/fxos8700/Kconfig#L92)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → FXOS8700 加速度计／磁力计（Accelerometer/Magnetometer）驱动 → 脉冲检测（Pulse Detection）

**配置项引用（Symbol References）**：[`CONFIG_FXOS8700_PULSE`](P153_drivers_sensor_配置项参考_5.md#CONFIG_FXOS8700_PULSE)、[`CONFIG_FXOS8700_TRIGGER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_FXOS8700_TRIGGER)、[`CONFIG_FXOS8700`](P153_drivers_sensor_配置项参考_5.md#CONFIG_FXOS8700)、[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_FXOS8700_TRIGGER`。

<a id="CONFIG_FXOS8700_TEMP"></a>

## 153.91 `CONFIG_FXOS8700_TEMP`

**提示（Prompt）**：温度（Temperature）

**说明（Help）**

启用温度传感器（Temperature Sensor）。注意，此温度传感器未经校准，对于相同温度，不同器件的输出可能不同。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(CONFIG_FXOS8700_MODE_MAGN || CONFIG_FXOS8700_MODE_HYBRID) && CONFIG_FXOS8700 && CONFIG_SENSOR
```

**定义位置（Location）**：[`drivers/sensor/nxp/fxos8700/Kconfig:35`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/nxp/fxos8700/Kconfig#L35)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → FXOS8700 加速度计／磁力计（Accelerometer/Magnetometer）驱动

**配置项引用（Symbol References）**：[`CONFIG_FXOS8700_MODE_MAGN`](P153_drivers_sensor_配置项参考_5.md#CONFIG_FXOS8700_MODE_MAGN)、[`CONFIG_FXOS8700_MODE_HYBRID`](P153_drivers_sensor_配置项参考_5.md#CONFIG_FXOS8700_MODE_HYBRID)、[`CONFIG_FXOS8700`](P153_drivers_sensor_配置项参考_5.md#CONFIG_FXOS8700)、[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)。

<a id="CONFIG_FXOS8700_THREAD_PRIORITY"></a>

## 153.92 `CONFIG_FXOS8700_THREAD_PRIORITY`

**提示（Prompt）**：专用线程优先级（Own Thread Priority）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_FXOS8700_TRIGGER_OWN_THREAD && CONFIG_FXOS8700_TRIGGER && CONFIG_FXOS8700 && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
10
```

**定义位置（Location）**：[`drivers/sensor/nxp/fxos8700/Kconfig:75`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/nxp/fxos8700/Kconfig#L75)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → FXOS8700 加速度计／磁力计（Accelerometer/Magnetometer）驱动

**配置项引用（Symbol References）**：[`CONFIG_FXOS8700_TRIGGER_OWN_THREAD`](P153_drivers_sensor_配置项参考_5.md#CONFIG_FXOS8700_TRIGGER_OWN_THREAD)、[`CONFIG_FXOS8700_TRIGGER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_FXOS8700_TRIGGER)、[`CONFIG_FXOS8700`](P153_drivers_sensor_配置项参考_5.md#CONFIG_FXOS8700)、[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_FXOS8700_TRIGGER`。

<a id="CONFIG_FXOS8700_THREAD_STACK_SIZE"></a>

## 153.93 `CONFIG_FXOS8700_THREAD_STACK_SIZE`

**提示（Prompt）**：专用线程栈大小（Own Thread Stack Size）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_FXOS8700_TRIGGER_OWN_THREAD && CONFIG_FXOS8700_TRIGGER && CONFIG_FXOS8700 && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
1024
```

**定义位置（Location）**：[`drivers/sensor/nxp/fxos8700/Kconfig:80`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/nxp/fxos8700/Kconfig#L80)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → FXOS8700 加速度计／磁力计（Accelerometer/Magnetometer）驱动

**配置项引用（Symbol References）**：[`CONFIG_FXOS8700_TRIGGER_OWN_THREAD`](P153_drivers_sensor_配置项参考_5.md#CONFIG_FXOS8700_TRIGGER_OWN_THREAD)、[`CONFIG_FXOS8700_TRIGGER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_FXOS8700_TRIGGER)、[`CONFIG_FXOS8700`](P153_drivers_sensor_配置项参考_5.md#CONFIG_FXOS8700)、[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_FXOS8700_TRIGGER`。

<a id="CONFIG_FXOS8700_TRIGGER_GLOBAL_THREAD"></a>

## 153.94 `CONFIG_FXOS8700_TRIGGER_GLOBAL_THREAD`

**提示（Prompt）**：使用全局线程（Global Thread）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_GPIO && (n || n) && <choice>
```

**主动选择（Selects）**

```text
CONFIG_FXOS8700_TRIGGER
```

**定义位置（Location）**：[`drivers/sensor/nxp/fxos8700/Kconfig:50`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/nxp/fxos8700/Kconfig#L50)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → FXOS8700 加速度计／磁力计（Accelerometer/Magnetometer）驱动 → 触发模式（Trigger Mode）

**配置项引用（Symbol References）**：[`CONFIG_GPIO`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO)、[`CONFIG_FXOS8700_TRIGGER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_FXOS8700_TRIGGER)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_FXOS8700_TRIGGER`。

<a id="CONFIG_FXOS8700_TRIGGER_NONE"></a>

## 153.95 `CONFIG_FXOS8700_TRIGGER_NONE`

**提示（Prompt）**：不触发（No Trigger）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`drivers/sensor/nxp/fxos8700/Kconfig:47`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/nxp/fxos8700/Kconfig#L47)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → FXOS8700 加速度计／磁力计（Accelerometer/Magnetometer）驱动 → 触发模式（Trigger Mode）

<a id="CONFIG_FXOS8700_TRIGGER_OWN_THREAD"></a>

## 153.96 `CONFIG_FXOS8700_TRIGGER_OWN_THREAD`

**提示（Prompt）**：使用专用线程（Own Thread）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**主动选择（Selects）**

```text
CONFIG_FXOS8700_TRIGGER
```

**定义位置（Location）**：[`drivers/sensor/nxp/fxos8700/Kconfig:57`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/nxp/fxos8700/Kconfig#L57)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → FXOS8700 加速度计／磁力计（Accelerometer/Magnetometer）驱动 → 触发模式（Trigger Mode）

**配置项引用（Symbol References）**：[`CONFIG_FXOS8700_TRIGGER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_FXOS8700_TRIGGER)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_FXOS8700_TRIGGER`。

<a id="CONFIG_GROVE_LIGHT_SENSOR"></a>

## 153.97 `CONFIG_GROVE_LIGHT_SENSOR`

**提示（Prompt）**：Seeed Grove 光照传感器（Light Sensor）

**说明（Help）**

设置此值将启用 Grove 光照传感器（Light Sensor）驱动支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_SEEED_GROVE_LIGHT_ENABLED && CONFIG_GROVE_SENSORS && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_ADC
```

**定义位置（Location）**：[`drivers/sensor/seeed/grove/Kconfig:15`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/seeed/grove/Kconfig#L15)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → Seeed Grove 传感器支持

**配置项引用（Symbol References）**：[`CONFIG_GROVE_SENSORS`](P153_drivers_sensor_配置项参考_5.md#CONFIG_GROVE_SENSORS)、[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)、[`CONFIG_ADC`](P047_drivers_adc_配置项参考_1.md#CONFIG_ADC)。

<a id="CONFIG_GROVE_SENSORS"></a>

## 153.98 `CONFIG_GROVE_SENSORS`

**提示（Prompt）**：Seeed Grove 传感器支持

**说明（Help）**

启用 Seeed Grove 传感器支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(DT_HAS_SEEED_GROVE_LIGHT_ENABLED || DT_HAS_SEEED_GROVE_TEMPERATURE_ENABLED) && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/sensor/seeed/grove/Kconfig:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/seeed/grove/Kconfig#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)。

<a id="CONFIG_GROVE_TEMPERATURE_SENSOR"></a>

## 153.99 `CONFIG_GROVE_TEMPERATURE_SENSOR`

**提示（Prompt）**：Seeed Grove 温度传感器（Temperature Sensor）

**说明（Help）**

设置此值将启用 Grove 温度传感器（Temperature Sensor）驱动支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_SEEED_GROVE_TEMPERATURE_ENABLED && CONFIG_GROVE_SENSORS && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_ADC
```

**定义位置（Location）**：[`drivers/sensor/seeed/grove/Kconfig:24`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/seeed/grove/Kconfig#L24)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → Seeed Grove 传感器支持

**配置项引用（Symbol References）**：[`CONFIG_GROVE_SENSORS`](P153_drivers_sensor_配置项参考_5.md#CONFIG_GROVE_SENSORS)、[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)、[`CONFIG_ADC`](P047_drivers_adc_配置项参考_1.md#CONFIG_ADC)。

<a id="CONFIG_GROW_R502A"></a>

## 153.100 `CONFIG_GROW_R502A`

**提示（Prompt）**：GROW_R502A 指纹传感器（Fingerprint Sensor）

**说明（Help）**

启用 GROW_R502A 指纹传感器（Fingerprint Sensor）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_HZGROW_R502A_ENABLED && CONFIG_UART_INTERRUPT_DRIVEN && CONFIG_SERIAL && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/sensor/grow_r502a/Kconfig:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/grow_r502a/Kconfig#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers）

**配置项引用（Symbol References）**：[`CONFIG_UART_INTERRUPT_DRIVEN`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_INTERRUPT_DRIVEN)、[`CONFIG_SERIAL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SERIAL)、[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)。

<!-- kconfig-navigation -->

[上一章](P152_drivers_sensor_配置项参考_4.md) · [返回大纲](大纲.md) · [下一章](P154_drivers_sensor_配置项参考_6.md)
