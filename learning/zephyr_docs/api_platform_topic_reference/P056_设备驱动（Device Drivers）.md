---
id: learning.zephyr-docs.api-platform-topic-reference.page-56
title: 设备驱动（Device Drivers）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__io__interfaces.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第56章\_设备驱动（Device Drivers）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__io__interfaces.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

与各类硬件外设交互的接口。

<a id="details"></a>

用于与各类硬件外设（Hardware Peripherals）交互的接口。这是一组与硬件无关（Hardware-Agnostic）的接口，用于实现设备驱动（Device Drivers）并与设备驱动交互。

<a id="header-groups"></a>
<a id="groups"></a>

## 56.1\_主题（Topics）

<a id="r_w1_5Finterface"></a>

相关声明：[单总线（1-Wire）](https://docs.zephyrproject.org/latest/doxygen/html/group__w1__interface.html)。

1-Wire 设备接口。

<a id="r_adc_5Finterface"></a>

相关声明：[模数转换器（ADC）](../hardware/P463_ADC公共接口参考.md)。

模数转换器（Analog-to-Digital Converter，ADC）接口。

<a id="r_audio_5Finterface"></a>

相关声明：[音频（Audio）](../api_topic_reference/P004_音频（Audio）.md)。

音频设备接口。

<a id="r_auxdisplay_5Finterface"></a>

相关声明：[辅助文本显示器（Auxiliary Text Display）](https://docs.zephyrproject.org/latest/doxygen/html/group__auxdisplay__interface.html)。

辅助显示器接口，适用于文本显示和非图形显示（Textual/non-graphical displays）。

<a id="r_bbram_5Finterface"></a>

相关声明：[电池备份 RAM（BBRAM）](https://docs.zephyrproject.org/latest/doxygen/html/group__bbram__interface.html)。

电池备份 RAM（Battery-Backed RAM，BBRAM）接口。

<a id="r_intc_5Fbcm283x"></a>

相关声明：[BCM283x 中断控制器（Interrupt controllers）](https://docs.zephyrproject.org/latest/doxygen/html/group__intc__bcm283x.html)。

<a id="r_charger_5Finterface"></a>

相关声明：[电池充电器（Battery Charger）](https://docs.zephyrproject.org/latest/doxygen/html/group__charger__interface.html)。

电池充电器接口。

<a id="r_biometrics_5Finterface"></a>

相关声明：[生物识别（Biometrics）](https://docs.zephyrproject.org/latest/doxygen/html/group__biometrics__interface.html)。

生物识别传感器（Biometric sensors）接口。

<a id="r_buzzer_5Finterface"></a>

相关声明：[蜂鸣器（Buzzer）](../hardware/P144_蜂鸣器接口参考.md)。

蜂鸣器接口。

<a id="r_can_5Finterface"></a>

相关声明：[控制器局域网（CAN）](../hardware/P361_CAN公共接口.md)。

控制器局域网（Controller Area Network，CAN）控制器与收发器接口。

<a id="r_crc_5Finterface"></a>

相关声明：[CRC 驱动 API（Driver APIs）](../hardware/P038_CRC驱动接口参考.md)。

循环冗余校验（Cyclic Redundancy Check，CRC）设备接口。

<a id="r_cellular_5Finterface"></a>

相关声明：[蜂窝通信（Cellular）](https://docs.zephyrproject.org/latest/doxygen/html/group__cellular__interface.html)。

蜂窝调制解调器（Cellular modems）接口。

<a id="r_clock_5Fcontrol_5Finterface"></a>

相关声明：[时钟控制（Clock Control）](../timer_reference/P092_时钟控制公共接口.md)。

时钟控制器接口。

<a id="r_clock_5Fmonitor_5Finterface"></a>

相关声明：[时钟监测器（Clock Monitor）](../timer_reference/P098_时钟监控公共接口.md)。

时钟监测器接口（Clock Monitor Interface）

<a id="r_comparator_5Finterface"></a>

相关声明：[比较器（Comparator）](../hardware/P089_比较器接口参考.md)。

比较器接口。

<a id="r_coredump_5Fdevice_5Finterface"></a>

相关声明：[核心转储伪设备（Coredump pseudo-device）](../observability/P053_核心转储设备接口.md)。

核心转储伪设备接口。

<a id="r_counter_5Finterface"></a>

相关声明：[计数器（Counter）](../timer_reference/P022_计数器公共接口.md)。

计数器接口。

<a id="r_dac_5Finterface"></a>

相关声明：[数模转换器（DAC）](../hardware/P822_数模转换器接口.md)。

数模转换器（Digital-to-Analog Converter）接口。

<a id="r_dai_5Finterface"></a>

相关声明：[数字音频接口（DAI）](https://docs.zephyrproject.org/latest/doxygen/html/group__dai__interface.html)。

数字音频接口（Digital Audio Interfaces）相关接口。

<a id="r_dali_5Finterface"></a>

相关声明：[数字可寻址照明接口（DALI）](https://docs.zephyrproject.org/latest/doxygen/html/group__dali__interface.html)。

DALI 接口（Interface）

<a id="r_dap_5Flink_5Finterface"></a>

相关声明：[调试访问端口链路（DAP Link）](https://docs.zephyrproject.org/latest/doxygen/html/group__dap__link__interface.html)。

调试访问端口（Debug Access Port，DAP）链路后端接口。

<a id="r_dma_5Finterface"></a>

相关声明：[直接内存访问（DMA）](../dma_reference/P001_DMA公共接口.md)。

直接内存访问（Direct Memory Access，DMA）控制器接口。

<a id="r_disk_5Fdriver_5Finterface"></a>

相关声明：[磁盘访问（Disk Access）](https://docs.zephyrproject.org/latest/doxygen/html/group__disk__driver__interface.html)。

磁盘接口。

<a id="r_display_5Finterface"></a>

相关声明：[显示（Display）](../hardware/P214_显示公共接口.md)。

显示控制器接口。

<a id="r_edac_5Finterface"></a>

相关声明：[错误检测与纠正（EDAC）](https://docs.zephyrproject.org/latest/doxygen/html/group__edac__interface.html)。

错误检测与纠正（Error Detection and Correction，EDAC）控制器接口。

<a id="r_eeprom_5Finterface"></a>

相关声明：[电可擦可编程只读存储器（EEPROM）](../hardware/P040_EEPROM接口参考.md)。

电可擦可编程只读存储器（Electrically Erasable Programmable Read-Only Memory，EEPROM）接口。

<a id="r_espi_5Finterface"></a>

相关声明：[增强串行外设接口（ESPI）](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html)。

增强串行外设接口（Enhanced Serial Peripheral Interface，eSPI）目标硬件接口。

<a id="r_entropy_5Finterface"></a>

相关声明：[熵（Entropy）](../hardware/P039_熵源接口参考.md)。

熵源硬件接口（Entropy hardware interfaces）。

<a id="r_cache_5Fexternal_5Finterface"></a>

相关声明：[外部缓存控制器（External Cache Controller）](../cache_reference/P004_外部缓存接口.md)。

外部缓存控制器接口（External Cache Controller Interfaces）。

<a id="r_fpga_5Finterface"></a>

相关声明：[现场可编程门阵列（FPGA）](https://docs.zephyrproject.org/latest/doxygen/html/group__fpga__interface.html)。

现场可编程门阵列（Field-Programmable Gate Arrays，FPGA）接口。

<a id="r_flash_5Finterface"></a>

相关声明：[闪存（Flash）](../flash_reference/P001_Flash公共接口.md)。

闪存控制器（Flash Memory Controller）的接口。

<a id="r_fuel_5Fgauge_5Finterface"></a>

相关声明：[电量计（Fuel Gauge）](https://docs.zephyrproject.org/latest/doxygen/html/group__fuel__gauge__interface.html)。

电量计接口。

<a id="r_gnss_5Finterface"></a>

相关声明：[全球导航卫星系统（GNSS）](https://docs.zephyrproject.org/latest/doxygen/html/group__gnss__interface.html)。

全球导航卫星系统（Global Navigation Satellite System，GNSS）接收机接口。

<a id="r_gpio_5Finterface"></a>

相关声明：[通用输入输出（GPIO）](../hardware/P266_GPIO公共接口.md)。

通用输入/输出（General Purpose Input/Output，GPIO）控制器接口。

<a id="r_haptics_5Finterface"></a>

相关声明：[触觉反馈（Haptics）](../hardware/P147_触觉反馈接口参考.md)。

触觉反馈驱动（Haptic drivers）接口。

<a id="r_hwinfo_5Finterface"></a>

相关声明：[硬件信息（Hardware Info）](../hardware_util_reference/P003_硬件信息公共接口.md)。

用于获取硬件信息（Hardware Information）的接口。

<a id="r_hwspinlock_5Finterface"></a>

相关声明：[硬件自旋锁（Hardware Spinlock）](../intercore_reference/P001_硬件自旋锁公共接口.md)。

硬件自旋锁接口。

<a id="r_i2c_5Finterface"></a>

相关声明：[集成电路间总线（I2C）](../hardware/P305_I2C公共接口.md)。

集成电路间总线（Inter-Integrated Circuit，I2C）控制器接口。

<a id="r_i2s_5Finterface"></a>

相关声明：[集成电路间音频总线（I2S）](https://docs.zephyrproject.org/latest/doxygen/html/group__i2s__interface.html)。

集成电路间音频（Inter-IC Sound，I2S）控制器接口。

<a id="r_i3c_5Finterface"></a>

相关声明：[改进型集成电路间总线（I3C）](../hardware/P425_I3C公共接口参考.md)。

改进型集成电路间总线（Improved Inter-Integrated Circuit，I3C）控制器接口。

<a id="r_ipm_5Finterface"></a>

相关声明：[处理器间邮箱（IPM）](../intercore_reference/P058_处理器间消息公共接口.md)。

处理器间邮箱（Inter-Processor Mailbox，IPM）控制器接口。

<a id="r_input_5Finterface"></a>

相关声明：[`input`（输入）。](https://docs.zephyrproject.org/latest/doxygen/html/group__input__interface.html)。

输入设备接口。

<a id="r_ivshmem"></a>

相关声明：[虚拟机间共享内存（Inter-VM Shared Memory）](../intercore_reference/P214_IVSHMEM共享内存接口.md)。

虚拟机间共享内存（Inter-VM Shared Memory，ivshmem）接口。

<a id="r_led_5Finterface"></a>

相关声明：[发光二极管（LED）](../hardware/P202_LED公共接口.md)。

发光二极管（Light-Emitting Diode，LED）控制器接口。

<a id="r_led_5Fstrip_5Finterface"></a>

相关声明：[LED 灯带（LED Strip）](../hardware/P208_LED灯带公共接口.md)。

LED 灯带接口。

<a id="r_lin_5Finterface"></a>

相关声明：[局部互连网络（LIN）](../api_topic_reference/P044_局部互连网络（LIN）.md)。

局部互连网络（Local Interconnect Network，LIN）控制器和收发器接口。

<a id="r_lora_5Finterface"></a>

相关声明：[LoRa](https://docs.zephyrproject.org/latest/doxygen/html/group__lora__interface.html)。

LoRa 收发器接口。

<a id="r_mbox_5Finterface"></a>

相关声明：[邮箱（MBOX）](../intercore_reference/P014_邮箱驱动公共接口.md)。

邮箱（Mailbox，MBOX）设备接口。

<a id="r_mdio_5Finterface"></a>

相关声明：[管理数据输入/输出（MDIO）](https://docs.zephyrproject.org/latest/doxygen/html/group__mdio__interface.html)。

管理数据输入/输出（Management Data Input/Output，MDIO）控制器接口。

<a id="r_memc_5Finterface"></a>

相关声明：[存储器控制器（MEMC）](https://docs.zephyrproject.org/latest/doxygen/html/group__memc__interface.html)。

存储器控制器（Memory Controller，MEMC）接口。

<a id="r_mspi_5Finterface"></a>

相关声明：[多位串行外设接口（MSPI）](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__interface.html)。

多位串行外设接口（Multi-bit Serial Peripheral Interface，MSPI）控制器接口。

<a id="r_mux_5Finterface"></a>

相关声明：[多路复用器（MUX）](https://docs.zephyrproject.org/latest/doxygen/html/group__mux__interface.html)。

MUX 控制器接口（MUX Controller Interface）

<a id="r_misc_5Finterfaces"></a>

相关声明：[其他设备（Miscellaneous Devices）](../api_topic_reference/P052_其他设备（Miscellaneous Devices）.md)。

没有专用驱动类别的硬件外设接口。

<a id="r_mfd_5Finterfaces"></a>

相关声明：[多功能设备（Multi-function Devices）](../api_topic_reference/P050_多功能设备（Multi-function Devices）.md)。

多功能设备接口。

<a id="r_nvmem_5Finterface"></a>

相关声明：[非易失性存储器（NVMEM）](../storage/P013_NVMEM接口参考.md)。

非易失性存储单元（Non-volatile memory cells）。

<a id="r_opamp_5Finterface"></a>

相关声明：[运算放大器（OPAMP）](../hardware/P091_运算放大器接口参考.md)。

运算放大器（Operational amplifier，OPAMP）接口。

<a id="r_otp_5Finterface"></a>

相关声明：[一次性可编程存储器（One Time Programmable Memory）](https://docs.zephyrproject.org/latest/doxygen/html/group__otp__interface.html)。

一次性可编程（One Time Programmable，OTP）存储器接口。

<a id="r_pcie_5Finterface"></a>

相关声明：[PCI Express（PCIe）](../api_topic_reference/P057_PCI Express（PCIe） API主题.md)。

PCIe 设备接口。

<a id="r_peci_5Finterface"></a>

相关声明：[平台环境控制接口（PECI）](https://docs.zephyrproject.org/latest/doxygen/html/group__peci__interface.html)。

平台环境控制接口（Platform Environment Control Interface，PECI）设备接口。

<a id="r_pmu"></a>

相关声明：[性能监控单元（PMU）](https://docs.zephyrproject.org/latest/doxygen/html/group__pmu.html)。

<a id="r_ps2_5Finterface"></a>

相关声明：[PS/2](https://docs.zephyrproject.org/latest/doxygen/html/group__ps2__interface.html)。

PS/2 设备接口。

<a id="r_psi5_5Finterface"></a>

相关声明：[外设传感器接口（PSI5）](https://docs.zephyrproject.org/latest/doxygen/html/group__psi5__interface.html)。

外设传感器接口（Peripheral Sensor Interface，PSI5）接口。

<a id="r_ptp_5Fclock_5Finterface"></a>

相关声明：[精确时间协议时钟（PTP Clock）](https://docs.zephyrproject.org/latest/doxygen/html/group__ptp__clock__interface.html)。

精确时间协议（Precision Time Protocol，PTP）时钟接口。

<a id="r_pwm_5Finterface"></a>

相关声明：[脉宽调制（PWM）](../hardware/P255_PWM公共接口.md)。

脉宽调制（Pulse Width Modulation，PWM）控制器接口。

<a id="r_pinctrl_5Finterface"></a>

相关声明：[引脚控制（Pin Control）](../pinctrl_reference/P001_引脚控制公共接口.md)。

引脚控制器（Pin Controller）接口。

<a id="r_pulse_5Fio_5Finterface"></a>

相关声明：[脉冲 I/O（Pulse IO）](https://docs.zephyrproject.org/latest/doxygen/html/group__pulse__io__interface.html)。

脉冲 I/O 接口（Pulse IO Interface）

<a id="r_qemu_5Ffwcfg_5Finterface"></a>

相关声明：[QEMU 固件配置（fw_cfg）](https://docs.zephyrproject.org/latest/doxygen/html/group__qemu__fwcfg__interface.html)。

QEMU 固件配置（Firmware configuration，fw_cfg）驱动接口。

<a id="r_rtc_5Finterface"></a>

相关声明：[实时时钟（RTC）](../timer_reference/P009_实时时钟公共接口.md)。

实时时钟（Real-time clock，RTC）接口。

<a id="r_regulator_5Finterface"></a>

相关声明：[稳压器（Regulator）](../power/P073_稳压器接口.md)。

稳压器接口。

<a id="r_reset_5Fcontroller_5Finterface"></a>

相关声明：[复位控制器（Reset Controller）](../reset_reference/P001_复位控制器公共接口.md)。

复位控制器（Reset Controller）的接口。

<a id="r_retained_5Fmem_5Finterface"></a>

相关声明：[保持存储器（Retained memory）](../hardware/P630_保留内存接口.md)。

保持存储器接口。

<a id="r_scmi_5Finterface"></a>

相关声明：[系统控制与管理接口（SCMI）](https://docs.zephyrproject.org/latest/doxygen/html/group__scmi__interface.html)。

ARM 系统控制与管理接口（System Control and Management Interface，SCMI）。

<a id="r_sdhc_5Finterface"></a>

相关声明：[安全数字主机控制器（SDHC）](https://docs.zephyrproject.org/latest/doxygen/html/group__sdhc__interface.html)。

安全数字主机控制器（Secure Digital Host Controller，SDHC）接口。

<a id="r_sent_5Finterface"></a>

相关声明：[单边沿半字节传输（SENT）](https://docs.zephyrproject.org/latest/doxygen/html/group__sent__interface.html)。

单边沿半字节传输（Single Edge Nibble Transmission，SENT）外设接口。

<a id="r_smbus_5Finterface"></a>

相关声明：[系统管理总线（SMBus）](https://docs.zephyrproject.org/latest/doxygen/html/group__smbus__interface.html)。

系统管理总线（System Management Bus，SMBus）接口。

<a id="r_spi_5Finterface"></a>

相关声明：[串行外设接口（SPI）](../hardware/P318_SPI公共接口.md)。

串行外设接口（Serial Peripheral Interface，SPI）控制器接口。

<a id="r_swdp_5Finterface"></a>

相关声明：[串行线调试端口（SWDP）](https://docs.zephyrproject.org/latest/doxygen/html/group__swdp__interface.html)。

串行线调试端口（Serial Wire Debug Port，SWDP）接口。

<a id="r_sensor_5Finterface"></a>

相关声明：[传感器（Sensor）](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html)。

传感器接口。

<a id="r_stepper_5Finterface"></a>

相关声明：[步进电机（Stepper）](../hardware/P229_步进电机接口目录.md)。

步进电机运动控制器和硬件驱动器接口。

<a id="r_syscon_5Finterface"></a>

相关声明：[系统控制（System control，SYSCON）](../syscon_reference/P001_系统控制器公共接口.md)。

系统控制寄存器（System Control Registers）的接口。

<a id="r_tee_5Finterface"></a>

相关声明：[可信执行环境（TEE）](https://docs.zephyrproject.org/latest/doxygen/html/group__tee__interface.html)。

与可信执行环境（Trusted Execution Environment，TEE）交互的接口。

<a id="r_tgpio_5Finterface"></a>

相关声明：[时间感知 GPIO（Time-aware GPIO）](../timer_reference/P191_时间感知GPIO公共接口.md)。

时间感知 GPIO 控制器接口。

<a id="r_uart_5Finterface"></a>

相关声明：[通用异步收发器（UART）](../hardware/P330_UART公共接口.md)。

通用异步收发器（Universal Asynchronous Receiver/Transmitter，UART）控制器接口。

<a id="r_usb_5Finterfaces"></a>

相关声明：[通用串行总线（USB）](../api_topic_reference/P104_通用串行总线（USB）.md)。

USB 硬件及相关标准的接口。

<a id="r_virtio_5Finterface"></a>

相关声明：[虚拟 I/O（VIRTIO）](../hardware/P571_VirtIO设备接口.md)。

虚拟 I/O（Virtual I/O，VIRTIO）设备接口。

<a id="r_video_5Finterface"></a>

相关声明：[视频驱动（Video Drivers）](https://docs.zephyrproject.org/latest/doxygen/html/group__video__interface.html)。

供视频子系统使用的视频驱动 API。

<a id="r_wuc_5Finterface"></a>

相关声明：[唤醒控制器（WUC）](https://docs.zephyrproject.org/latest/doxygen/html/group__wuc__interface.html)。

唤醒控制器（Wakeup Controller，WUC）驱动 API。

<a id="r_watchdog_5Finterface"></a>

相关声明：[看门狗（Watchdog）](../timer_reference/P001_看门狗公共接口.md)。

看门狗设备接口。


## 56.2\_原页交叉引用（Cross References）

- [单总线（1-Wire）](https://docs.zephyrproject.org/latest/doxygen/html/group__w1__interface.html)
- [模数转换器（ADC）](../hardware/P463_ADC公共接口参考.md)
- [音频（Audio）](../api_topic_reference/P004_音频（Audio）.md)
- [辅助文本显示器（Auxiliary Text Display）](https://docs.zephyrproject.org/latest/doxygen/html/group__auxdisplay__interface.html)
- [电池备份 RAM（BBRAM）](https://docs.zephyrproject.org/latest/doxygen/html/group__bbram__interface.html)
- [BCM283x 中断控制器（Interrupt controllers）](https://docs.zephyrproject.org/latest/doxygen/html/group__intc__bcm283x.html)
- [电池充电器（Battery Charger）](https://docs.zephyrproject.org/latest/doxygen/html/group__charger__interface.html)
- [生物识别（Biometrics）](https://docs.zephyrproject.org/latest/doxygen/html/group__biometrics__interface.html)
- [蜂鸣器（Buzzer）](../hardware/P144_蜂鸣器接口参考.md)
- [控制器局域网（CAN）](../hardware/P361_CAN公共接口.md)
- [CRC 驱动 API（Driver APIs）](../hardware/P038_CRC驱动接口参考.md)
- [蜂窝通信（Cellular）](https://docs.zephyrproject.org/latest/doxygen/html/group__cellular__interface.html)
- [时钟控制（Clock Control）](../timer_reference/P092_时钟控制公共接口.md)
- [时钟监测器（Clock Monitor）](../timer_reference/P098_时钟监控公共接口.md)
- [比较器（Comparator）](../hardware/P089_比较器接口参考.md)
- [核心转储伪设备（Coredump pseudo-device）](../observability/P053_核心转储设备接口.md)
- [计数器（Counter）](../timer_reference/P022_计数器公共接口.md)
- [数模转换器（DAC）](../hardware/P822_数模转换器接口.md)
- [数字音频接口（DAI）](https://docs.zephyrproject.org/latest/doxygen/html/group__dai__interface.html)
- [数字可寻址照明接口（DALI）](https://docs.zephyrproject.org/latest/doxygen/html/group__dali__interface.html)
- [调试访问端口链路（DAP Link）](https://docs.zephyrproject.org/latest/doxygen/html/group__dap__link__interface.html)
- [直接内存访问（DMA）](../dma_reference/P001_DMA公共接口.md)
- [磁盘访问（Disk Access）](https://docs.zephyrproject.org/latest/doxygen/html/group__disk__driver__interface.html)
- [显示（Display）](../hardware/P214_显示公共接口.md)
- [错误检测与纠正（EDAC）](https://docs.zephyrproject.org/latest/doxygen/html/group__edac__interface.html)
- [电可擦可编程只读存储器（EEPROM）](../hardware/P040_EEPROM接口参考.md)
- [增强串行外设接口（ESPI）](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html)
- [熵（Entropy）](../hardware/P039_熵源接口参考.md)
- [外部缓存控制器（External Cache Controller）](../cache_reference/P004_外部缓存接口.md)
- [现场可编程门阵列（FPGA）](https://docs.zephyrproject.org/latest/doxygen/html/group__fpga__interface.html)
- [闪存（Flash）](../flash_reference/P001_Flash公共接口.md)
- [电量计（Fuel Gauge）](https://docs.zephyrproject.org/latest/doxygen/html/group__fuel__gauge__interface.html)
- [全球导航卫星系统（GNSS）](https://docs.zephyrproject.org/latest/doxygen/html/group__gnss__interface.html)
- [通用输入输出（GPIO）](../hardware/P266_GPIO公共接口.md)
- [触觉反馈（Haptics）](../hardware/P147_触觉反馈接口参考.md)
- [硬件信息（Hardware Info）](../hardware_util_reference/P003_硬件信息公共接口.md)
- [硬件自旋锁（Hardware Spinlock）](../intercore_reference/P001_硬件自旋锁公共接口.md)
- [集成电路间总线（I2C）](../hardware/P305_I2C公共接口.md)
- [集成电路间音频总线（I2S）](https://docs.zephyrproject.org/latest/doxygen/html/group__i2s__interface.html)
- [改进型集成电路间总线（I3C）](../hardware/P425_I3C公共接口参考.md)
- [处理器间邮箱（IPM）](../intercore_reference/P058_处理器间消息公共接口.md)
- [`input`（输入）。](https://docs.zephyrproject.org/latest/doxygen/html/group__input__interface.html)
- [虚拟机间共享内存（Inter-VM Shared Memory）](../intercore_reference/P214_IVSHMEM共享内存接口.md)
- [发光二极管（LED）](../hardware/P202_LED公共接口.md)
- [LED 灯带（LED Strip）](../hardware/P208_LED灯带公共接口.md)
- [局部互连网络（LIN）](../api_topic_reference/P044_局部互连网络（LIN）.md)
- [LoRa](https://docs.zephyrproject.org/latest/doxygen/html/group__lora__interface.html)
- [邮箱（MBOX）](../intercore_reference/P014_邮箱驱动公共接口.md)
- [管理数据输入/输出（MDIO）](https://docs.zephyrproject.org/latest/doxygen/html/group__mdio__interface.html)
- [存储器控制器（MEMC）](https://docs.zephyrproject.org/latest/doxygen/html/group__memc__interface.html)
- [多位串行外设接口（MSPI）](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__interface.html)
- [多路复用器（MUX）](https://docs.zephyrproject.org/latest/doxygen/html/group__mux__interface.html)
- [其他设备（Miscellaneous Devices）](../api_topic_reference/P052_其他设备（Miscellaneous Devices）.md)
- [多功能设备（Multi-function Devices）](../api_topic_reference/P050_多功能设备（Multi-function Devices）.md)
- [非易失性存储器（NVMEM）](../storage/P013_NVMEM接口参考.md)
- [运算放大器（OPAMP）](../hardware/P091_运算放大器接口参考.md)
- [一次性可编程存储器（One Time Programmable Memory）](https://docs.zephyrproject.org/latest/doxygen/html/group__otp__interface.html)
- [PCI Express（PCIe）](../api_topic_reference/P057_PCI Express（PCIe） API主题.md)
- [平台环境控制接口（PECI）](https://docs.zephyrproject.org/latest/doxygen/html/group__peci__interface.html)
- [性能监控单元（PMU）](https://docs.zephyrproject.org/latest/doxygen/html/group__pmu.html)
- [PS/2](https://docs.zephyrproject.org/latest/doxygen/html/group__ps2__interface.html)
- [外设传感器接口（PSI5）](https://docs.zephyrproject.org/latest/doxygen/html/group__psi5__interface.html)
- [精确时间协议时钟（PTP Clock）](https://docs.zephyrproject.org/latest/doxygen/html/group__ptp__clock__interface.html)
- [脉宽调制（PWM）](../hardware/P255_PWM公共接口.md)
- [引脚控制（Pin Control）](../pinctrl_reference/P001_引脚控制公共接口.md)
- [脉冲 I/O（Pulse IO）](https://docs.zephyrproject.org/latest/doxygen/html/group__pulse__io__interface.html)
- [QEMU 固件配置（fw_cfg）](https://docs.zephyrproject.org/latest/doxygen/html/group__qemu__fwcfg__interface.html)
- [实时时钟（RTC）](../timer_reference/P009_实时时钟公共接口.md)
- [稳压器（Regulator）](../power/P073_稳压器接口.md)
- [复位控制器（Reset Controller）](../reset_reference/P001_复位控制器公共接口.md)
- [保持存储器（Retained memory）](../hardware/P630_保留内存接口.md)
- [系统控制与管理接口（SCMI）](https://docs.zephyrproject.org/latest/doxygen/html/group__scmi__interface.html)
- [安全数字主机控制器（SDHC）](https://docs.zephyrproject.org/latest/doxygen/html/group__sdhc__interface.html)
- [单边沿半字节传输（SENT）](https://docs.zephyrproject.org/latest/doxygen/html/group__sent__interface.html)
- [系统管理总线（SMBus）](https://docs.zephyrproject.org/latest/doxygen/html/group__smbus__interface.html)
- [串行外设接口（SPI）](../hardware/P318_SPI公共接口.md)
- [串行线调试端口（SWDP）](https://docs.zephyrproject.org/latest/doxygen/html/group__swdp__interface.html)
- [传感器（Sensor）](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html)
- [步进电机（Stepper）](../hardware/P229_步进电机接口目录.md)
- [系统控制（System control，SYSCON）](../syscon_reference/P001_系统控制器公共接口.md)
- [可信执行环境（TEE）](https://docs.zephyrproject.org/latest/doxygen/html/group__tee__interface.html)
- [时间感知 GPIO（Time-aware GPIO）](../timer_reference/P191_时间感知GPIO公共接口.md)
- [通用异步收发器（UART）](../hardware/P330_UART公共接口.md)
- [通用串行总线（USB）](../api_topic_reference/P104_通用串行总线（USB）.md)
- [虚拟 I/O（VIRTIO）](../hardware/P571_VirtIO设备接口.md)
- [视频驱动（Video Drivers）](https://docs.zephyrproject.org/latest/doxygen/html/group__video__interface.html)
- [视频子系统（Video Subsystem）](P128_视频子系统（Video Subsystem）.md)
- [唤醒控制器（WUC）](https://docs.zephyrproject.org/latest/doxygen/html/group__wuc__interface.html)
- [看门狗（Watchdog）](../timer_reference/P001_看门狗公共接口.md)

<a id="header-details"></a>

---

[上一章](P055_IEEE 802.15.4 与 Thread API.md) · [返回大纲](大纲.md) · [下一章](P057_日志记录器系统（Logger System）.md)
