---
id: learning.zephyr-docs.kconfig-reference.page-417
title: "`subsys/random`配置项参考"
kind: reference
status: evolving
domains: [zephyr, kconfig, configuration]
source_url: https://docs.zephyrproject.org/latest/kconfig.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；分册、相对路径和明确标注的译注为本地新增。 -->

# 第417章\_`subsys/random`配置项参考

本章翻译官方 Kconfig 数据库中 `subsys/random` 的 16 条定义记录。提示（Prompt）、帮助（Help）与菜单路径均已翻译；条件表达式和配置标识符保持原样，默认值除有译注明示的构建机路径相对化外保留原值。原页：[Kconfig Search](https://docs.zephyrproject.org/latest/kconfig.html)。来源数据库版本为 `main`，快照摘要与完整覆盖范围见[本册大纲](大纲.md)。

`main` 源码链接随上游变化；行号来自本次数据库快照，不能视为固定提交定位。无提示的配置项保留其不可直接由用户赋值的属性。原库中存在未收录定义的交叉引用，本章在对应位置明确标出。

<a id="CONFIG_ARM64_RANDOM_GENERATOR"></a>

## 417.1 `CONFIG_ARM64_RANDOM_GENERATOR`

**提示（Prompt）**：使用 ARM64 伪随机数生成器（PRNG）

**说明（Help）**

启用基于 ARM 扩展 `FEAT_RNG` 中 `RNDR` 指令的伪随机数生成器（Pseudo-random number generator）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ARM64_RNG && <choice CONFIG_RNG_GENERATOR_CHOICE>
```

**定义位置（Location）**：[`subsys/random/Kconfig:78`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/random/Kconfig#L78)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 随机数生成器（Random Number Generators） → 随机数生成器（Random generator）

**配置项引用（Symbol References）**：[`CONFIG_ARM64_RNG`](P031_arch_arm64_配置项参考.md#CONFIG_ARM64_RNG)、[`CONFIG_RNG_GENERATOR_CHOICE`](P417_subsys_random_配置项参考.md#CONFIG_RNG_GENERATOR_CHOICE)。

<a id="CONFIG_ARM64_RANDOM_GENERATOR_MAX_RETRIES"></a>

## 417.2 `CONFIG_ARM64_RANDOM_GENERATOR_MAX_RETRIES`

**提示（Prompt）**：ARM64 随机数生成器的最大重试次数（Retries）

**说明（Help）**

`RNDR` 指令连续失败达到多少次后，随机数生成器放弃。由于无法返回错误，此时会触发内核致命错误（Kernel panic）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_ARM64_RANDOM_GENERATOR
```

**默认值（Defaults）**

```text
10
```

**定义位置（Location）**：[`subsys/random/Kconfig:89`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/random/Kconfig#L89)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 随机数生成器（Random Number Generators）

**配置项引用（Symbol References）**：[`CONFIG_ARM64_RANDOM_GENERATOR`](P417_subsys_random_配置项参考.md#CONFIG_ARM64_RANDOM_GENERATOR)。

<a id="CONFIG_ARM64_RANDOM_GENERATOR_RETRY_WAIT_USEC"></a>

## 417.3 `CONFIG_ARM64_RANDOM_GENERATOR_RETRY_WAIT_USEC`

**提示（Prompt）**：ARM64 随机数生成器的重试等待时间（Retry wait time）

**说明（Help）**

`RNDR` 指令失败后，生成器再次尝试前应等待的微秒数。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_ARM64_RANDOM_GENERATOR
```

**默认值（Defaults）**

```text
500
```

**定义位置（Location）**：[`subsys/random/Kconfig:97`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/random/Kconfig#L97)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 随机数生成器（Random Number Generators）

**配置项引用（Symbol References）**：[`CONFIG_ARM64_RANDOM_GENERATOR`](P417_subsys_random_配置项参考.md#CONFIG_ARM64_RANDOM_GENERATOR)。

<a id="CONFIG_CSPRNG_ENABLED"></a>

## 417.4 `CONFIG_CSPRNG_ENABLED`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

辅助符号，用于确认构建中已启用一个硬件熵单元（Hardware entropy unit），能够提供密码学安全（Cryptographically secure，CS）的随机值。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ENTROPY_HAS_DRIVER
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/random/Kconfig:139`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/random/Kconfig#L139)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 随机数生成器（Random Number Generators）

**配置项引用（Symbol References）**：[`CONFIG_ENTROPY_HAS_DRIVER`](P084_drivers_entropy_配置项参考.md#CONFIG_ENTROPY_HAS_DRIVER)。

<a id="CONFIG_CSPRNG_GENERATOR_CHOICE"></a>

## 417.5 `CONFIG_CSPRNG_GENERATOR_CHOICE`

**提示（Prompt）**：密码学安全随机数生成器（Cryptographically Secure Random Number Generator）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**默认值（Defaults）**

```text
CONFIG_PSA_CSPRNG_GENERATOR if CONFIG_ENTROPY_NEEDS_PRNG
CONFIG_HARDWARE_DEVICE_CS_GENERATOR
CONFIG_TEST_CSPRNG_GENERATOR
```

**可选项（Choices）**

```text
CONFIG_HARDWARE_DEVICE_CS_GENERATOR
CONFIG_PSA_CSPRNG_GENERATOR
CONFIG_TEST_CSPRNG_GENERATOR
```

**定义位置（Location）**：[`subsys/random/Kconfig:148`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/random/Kconfig#L148)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 随机数生成器（Random Number Generators）

**配置项引用（Symbol References）**：[`CONFIG_PSA_CSPRNG_GENERATOR`](P417_subsys_random_配置项参考.md#CONFIG_PSA_CSPRNG_GENERATOR)、[`CONFIG_ENTROPY_NEEDS_PRNG`](P084_drivers_entropy_配置项参考.md#CONFIG_ENTROPY_NEEDS_PRNG)、[`CONFIG_HARDWARE_DEVICE_CS_GENERATOR`](P417_subsys_random_配置项参考.md#CONFIG_HARDWARE_DEVICE_CS_GENERATOR)、[`CONFIG_TEST_CSPRNG_GENERATOR`](P417_subsys_random_配置项参考.md#CONFIG_TEST_CSPRNG_GENERATOR)。

<a id="CONFIG_CSPRNG_NEEDED"></a>

## 417.6 `CONFIG_CSPRNG_NEEDED`

**提示（Prompt）**：当前平台允许时使用密码学安全随机数生成器（CSPRNG）

**说明（Help）**

如果设备树（DT）中存在熵生成器（Entropy generator）节点，即已设置 `CONFIG_ENTROPY_NODE_ENABLED`，则启用本符号，再检查 `CONFIG_CSPRNG_ENABLED` 的“结果”，确认对应驱动是否确实包含在构建中。这可确保：平台确实有熵驱动；且仅在有组件需要时才启用它。

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_ENTROPY_GENERATOR if CONFIG_ENTROPY_NODE_ENABLED
```

**被选择（Selected by）**

```text
CONFIG_SILABS_SISDK_CRYPTO
CONFIG_MBEDTLS_PSA_CRYPTO_C
CONFIG_SILABS_SISDK_CRYPTO
CONFIG_MBEDTLS_PSA_CRYPTO_C
CONFIG_ARM_PAC_PER_THREAD
CONFIG_QUIC
```

**定义位置（Location）**：[`subsys/random/Kconfig:124`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/random/Kconfig#L124)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 随机数生成器（Random Number Generators）

**配置项引用（Symbol References）**：[`CONFIG_ENTROPY_GENERATOR`](P084_drivers_entropy_配置项参考.md#CONFIG_ENTROPY_GENERATOR)、[`CONFIG_ENTROPY_NODE_ENABLED`](P417_subsys_random_配置项参考.md#CONFIG_ENTROPY_NODE_ENABLED)、[`CONFIG_SILABS_SISDK_CRYPTO`](P233_modules_hal_silabs_配置项参考.md#CONFIG_SILABS_SISDK_CRYPTO)、[`CONFIG_MBEDTLS_PSA_CRYPTO_C`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS_PSA_CRYPTO_C)、[`CONFIG_ARM_PAC_PER_THREAD`](P032_arch_common_配置项参考.md#CONFIG_ARM_PAC_PER_THREAD)、[`CONFIG_QUIC`](P407_subsys_net_配置项参考_17.md#CONFIG_QUIC)。

<a id="CONFIG_ENTROPY_DEVICE_RANDOM_GENERATOR"></a>

## 417.7 `CONFIG_ENTROPY_DEVICE_RANDOM_GENERATOR`

**提示（Prompt）**：使用熵驱动（Entropy driver）生成随机数

**说明（Help）**

启用随机数生成器（Random number generator），使用已启用的硬件熵采集驱动生成随机数。只有硬件熵驱动设计为可充当随机数生成源时，才应选择此项。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ENTROPY_HAS_DRIVER && <choice CONFIG_RNG_GENERATOR_CHOICE>
```

**定义位置（Location）**：[`subsys/random/Kconfig:61`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/random/Kconfig#L61)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 随机数生成器（Random Number Generators） → 随机数生成器（Random generator）

**配置项引用（Symbol References）**：[`CONFIG_ENTROPY_HAS_DRIVER`](P084_drivers_entropy_配置项参考.md#CONFIG_ENTROPY_HAS_DRIVER)、[`CONFIG_RNG_GENERATOR_CHOICE`](P417_subsys_random_配置项参考.md#CONFIG_RNG_GENERATOR_CHOICE)。

<a id="CONFIG_ENTROPY_NODE_ENABLED"></a>

## 417.8 `CONFIG_ENTROPY_NODE_ENABLED`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

辅助符号，表示设备树（DT）的 `zephyr,entropy` 属性指向一个熵生成单元（Entropy generator unit）节点。警告一：即便设置了此属性，也不能保证启用 `CONFIG_ENTROPY_GENERATOR` 后对应驱动一定可用，因为驱动可能还受其他未启用 Kconfig 选项约束。警告二：即使在 `CONFIG_ENTROPY_NODE_ENABLED` 设置后直接启用 `CONFIG_ENTROPY_GENERATOR` 能正常工作，也未必适合所有场景，因为没有任何组件使用它时，驱动仍会被启用。原文给出的解决办法是尝试启用 `CONFIG_CSPRNG_NEEDED`，然后检查 `CONFIG_CSPRNG_ENABLED` 的“返回值”。

**类型（Type）**：布尔值（Boolean），`bool`。

**默认值（Defaults）**

```text
y if n
```

**定义位置（Location）**：[`subsys/random/Kconfig:107`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/random/Kconfig#L107)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 随机数生成器（Random Number Generators）

<a id="CONFIG_HARDWARE_DEVICE_CS_GENERATOR"></a>

## 417.9 `CONFIG_HARDWARE_DEVICE_CS_GENERATOR`

**提示（Prompt）**：使用硬件随机数驱动生成密码学安全（CS）随机数

**说明（Help）**

启用密码学安全随机数生成器（Cryptographically secure random number generator），通过已启用的硬件随机数驱动生成随机数。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ENTROPY_HAS_DRIVER && <choice CONFIG_CSPRNG_GENERATOR_CHOICE>
```

**定义位置（Location）**：[`subsys/random/Kconfig:154`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/random/Kconfig#L154)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 随机数生成器（Random Number Generators） → 密码学安全随机数生成器（Cryptographically Secure Random Number Generator）

**配置项引用（Symbol References）**：[`CONFIG_ENTROPY_HAS_DRIVER`](P084_drivers_entropy_配置项参考.md#CONFIG_ENTROPY_HAS_DRIVER)、[`CONFIG_CSPRNG_GENERATOR_CHOICE`](P417_subsys_random_配置项参考.md#CONFIG_CSPRNG_GENERATOR_CHOICE)。

<a id="CONFIG_PSA_CSPRNG_GENERATOR"></a>

## 417.10 `CONFIG_PSA_CSPRNG_GENERATOR`

**提示（Prompt）**：使用 PSA 密码学安全随机数生成器（CSPRNG）

**说明（Help）**

启用使用 PSA Crypto API 的密码学安全随机数生成器（CSPRNG）。此实现采用底层 PSA Crypto 库的安全随机数生成功能，硬件熵源（Hardware entropy source）可用时可能使用该熵源。PSA CSPRNG 提供适用于安全敏感应用的密码学安全随机数。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_PSA_CRYPTO && <choice CONFIG_CSPRNG_GENERATOR_CHOICE>
```

**定义位置（Location）**：[`subsys/random/Kconfig:162`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/random/Kconfig#L162)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 随机数生成器（Random Number Generators） → 密码学安全随机数生成器（Cryptographically Secure Random Number Generator）

**配置项引用（Symbol References）**：[`CONFIG_PSA_CRYPTO`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_CRYPTO)、[`CONFIG_CSPRNG_GENERATOR_CHOICE`](P417_subsys_random_配置项参考.md#CONFIG_CSPRNG_GENERATOR_CHOICE)。

<a id="CONFIG_RNG_GENERATOR_CHOICE"></a>

## 417.11 `CONFIG_RNG_GENERATOR_CHOICE`

**提示（Prompt）**：随机数生成器（Random generator）

**说明（Help）**

平台相关的非密码学安全随机数（Non-cryptographically secure random number）支持。如果平台熵支持的性能足以满足随机数请求，则选择该来源；否则选择 XOSHIRO 算法。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ENTROPY_HAS_DRIVER || CONFIG_TEST_RANDOM_GENERATOR || CONFIG_ARM64_RNG
```

**默认值（Defaults）**

```text
CONFIG_ARM64_RANDOM_GENERATOR if CONFIG_ARM64_RNG
CONFIG_ENTROPY_DEVICE_RANDOM_GENERATOR if CONFIG_ENTROPY_HAS_DRIVER && !CONFIG_ENTROPY_NEEDS_PRNG
CONFIG_XOSHIRO_RANDOM_GENERATOR if CONFIG_ENTROPY_HAS_DRIVER && CONFIG_ENTROPY_NEEDS_PRNG
CONFIG_TIMER_RANDOM_GENERATOR if CONFIG_TEST_RANDOM_GENERATOR
```

**可选项（Choices）**

```text
CONFIG_TIMER_RANDOM_GENERATOR
CONFIG_ENTROPY_DEVICE_RANDOM_GENERATOR
CONFIG_XOSHIRO_RANDOM_GENERATOR
CONFIG_ARM64_RANDOM_GENERATOR
```

**其他位置的默认值（Other Defaults）**

来源：[`subsys/testsuite/Kconfig.defconfig`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/testsuite/Kconfig.defconfig)。

```text
CONFIG_XOSHIRO_RANDOM_GENERATOR if CONFIG_ZTRESS && CONFIG_ENTROPY_HAS_DRIVER
```

**定义位置（Location）**：[`subsys/random/Kconfig:39`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/random/Kconfig#L39)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 随机数生成器（Random Number Generators）

**配置项引用（Symbol References）**：[`CONFIG_ENTROPY_HAS_DRIVER`](P084_drivers_entropy_配置项参考.md#CONFIG_ENTROPY_HAS_DRIVER)、[`CONFIG_TEST_RANDOM_GENERATOR`](P417_subsys_random_配置项参考.md#CONFIG_TEST_RANDOM_GENERATOR)、[`CONFIG_ARM64_RNG`](P031_arch_arm64_配置项参考.md#CONFIG_ARM64_RNG)、[`CONFIG_ARM64_RANDOM_GENERATOR`](P417_subsys_random_配置项参考.md#CONFIG_ARM64_RANDOM_GENERATOR)、[`CONFIG_ENTROPY_DEVICE_RANDOM_GENERATOR`](P417_subsys_random_配置项参考.md#CONFIG_ENTROPY_DEVICE_RANDOM_GENERATOR)、[`CONFIG_ENTROPY_NEEDS_PRNG`](P084_drivers_entropy_配置项参考.md#CONFIG_ENTROPY_NEEDS_PRNG)、[`CONFIG_XOSHIRO_RANDOM_GENERATOR`](P417_subsys_random_配置项参考.md#CONFIG_XOSHIRO_RANDOM_GENERATOR)、[`CONFIG_TIMER_RANDOM_GENERATOR`](P417_subsys_random_配置项参考.md#CONFIG_TIMER_RANDOM_GENERATOR)、[`CONFIG_ZTRESS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ZTRESS)。

<a id="CONFIG_TEST_CSPRNG_GENERATOR"></a>

## 417.12 `CONFIG_TEST_CSPRNG_GENERATOR`

**提示（Prompt）**：为测试使用不安全的密码学安全随机数生成器（Insecure CSPRNG）

**说明（Help）**

将 `sys_csrand_get` 调用转交给 `sys_rand_get`，使使用前者的库能够通过 ZTEST 进行测试。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_TEST_RANDOM_GENERATOR && <choice CONFIG_CSPRNG_GENERATOR_CHOICE>
```

**定义位置（Location）**：[`subsys/random/Kconfig:174`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/random/Kconfig#L174)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 随机数生成器（Random Number Generators） → 密码学安全随机数生成器（Cryptographically Secure Random Number Generator）

**配置项引用（Symbol References）**：[`CONFIG_TEST_RANDOM_GENERATOR`](P417_subsys_random_配置项参考.md#CONFIG_TEST_RANDOM_GENERATOR)、[`CONFIG_CSPRNG_GENERATOR_CHOICE`](P417_subsys_random_配置项参考.md#CONFIG_CSPRNG_GENERATOR_CHOICE)。

<a id="CONFIG_TEST_RANDOM_GENERATOR"></a>

## 417.13 `CONFIG_TEST_RANDOM_GENERATOR`

**提示（Prompt）**：允许非随机数生成器（Non-random number generator）

**说明（Help）**

表示允许使用非随机数生成器（Non-random number generator），并允许内核随机数 API 返回并非真正随机的值。此能力用于没有真正随机数生成器时进行测试，不应在生产环境使用。此选项应仅由测试和示例等应用层配置选择，表示应用允许使用不具备真正随机性的生成器。开发板层配置不得选择此项，除非该开发板专用于测试，例如 QEMU 仿真开发板。注意，此选项并不表示已选择非随机数生成器，实际选择由 `RNG_GENERATOR_CHOICE` 决定。即使 `CONFIG_TEST_RANDOM_GENERATOR=y`，存在基于熵设备（Entropy device）的随机数生成器时，仍默认选择该生成器。

**类型（Type）**：布尔值（Boolean），`bool`。

**被选择（Selected by）**

```text
CONFIG_MBEDTLS_PSA_CRYPTO_LEGACY_RNG
CONFIG_MBEDTLS_PSA_CRYPTO_LEGACY_RNG
CONFIG_ZTEST_SHUFFLE
CONFIG_ZTRESS
```

**被弱选择（Implied by）**

```text
CONFIG_ARM_PAC_PER_THREAD
```

**定义位置（Location）**：[`subsys/random/Kconfig:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/random/Kconfig#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 随机数生成器（Random Number Generators）

**配置项引用（Symbol References）**：[`CONFIG_MBEDTLS_PSA_CRYPTO_LEGACY_RNG`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS_PSA_CRYPTO_LEGACY_RNG)、[`CONFIG_ZTEST_SHUFFLE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ZTEST_SHUFFLE)、[`CONFIG_ZTRESS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ZTRESS)、[`CONFIG_ARM_PAC_PER_THREAD`](P032_arch_common_配置项参考.md#CONFIG_ARM_PAC_PER_THREAD)。

<a id="CONFIG_TIMER_RANDOM_GENERATOR"></a>

## 417.14 `CONFIG_TIMER_RANDOM_GENERATOR`

**提示（Prompt）**：基于系统定时器时钟的数值生成器（System timer clock-based number generator）

**说明（Help）**

启用基于系统定时器时钟的数值生成器（Number generator）。它不具有随机性，仅供测试使用。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_TEST_RANDOM_GENERATOR && <choice CONFIG_RNG_GENERATOR_CHOICE>
```

**定义位置（Location）**：[`subsys/random/Kconfig:53`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/random/Kconfig#L53)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 随机数生成器（Random Number Generators） → 随机数生成器（Random generator）

**配置项引用（Symbol References）**：[`CONFIG_TEST_RANDOM_GENERATOR`](P417_subsys_random_配置项参考.md#CONFIG_TEST_RANDOM_GENERATOR)、[`CONFIG_RNG_GENERATOR_CHOICE`](P417_subsys_random_配置项参考.md#CONFIG_RNG_GENERATOR_CHOICE)。

<a id="CONFIG_TIMER_RANDOM_INITIAL_STATE"></a>

## 417.15 `CONFIG_TIMER_RANDOM_INITIAL_STATE`

**提示（Prompt）**：基于时钟的数值生成器所用初始状态（Initial state）

**说明（Help）**

`TIMER_RANDOM_GENERATOR` 及早期随机数生成器（Early random number generator）使用的初始状态值。

**类型（Type）**：整数（Integer），`int`。

**默认值（Defaults）**

```text
123456789
```

**定义位置（Location）**：[`subsys/random/Kconfig:31`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/random/Kconfig#L31)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 随机数生成器（Random Number Generators）

<a id="CONFIG_XOSHIRO_RANDOM_GENERATOR"></a>

## 417.16 `CONFIG_XOSHIRO_RANDOM_GENERATOR`

**提示（Prompt）**：使用 Xoshiro128++ 伪随机数生成器（PRNG）

**说明（Help）**

启用 Xoshiro128++ 伪随机数生成器（Pseudo-random number generator），以熵驱动（Entropy driver）作为种子来源。这是快速、通用且非密码学安全（Non-cryptographically secure）的随机数生成器。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ENTROPY_HAS_DRIVER && <choice CONFIG_RNG_GENERATOR_CHOICE>
```

**定义位置（Location）**：[`subsys/random/Kconfig:70`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/random/Kconfig#L70)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 随机数生成器（Random Number Generators） → 随机数生成器（Random generator）

**配置项引用（Symbol References）**：[`CONFIG_ENTROPY_HAS_DRIVER`](P084_drivers_entropy_配置项参考.md#CONFIG_ENTROPY_HAS_DRIVER)、[`CONFIG_RNG_GENERATOR_CHOICE`](P417_subsys_random_配置项参考.md#CONFIG_RNG_GENERATOR_CHOICE)。

<!-- kconfig-navigation -->

[上一章](P416_subsys_profiling_配置项参考.md) · [返回大纲](大纲.md) · [下一章](P418_subsys_retention_配置项参考.md)
