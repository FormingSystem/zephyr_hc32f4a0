---
id: learning.zephyr-docs.hardware.canapi-1
title: CAN控制器接口
kind: reference
status: maintained
domains: [zephyr, hardware]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__can__controller.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第362章\_CAN控制器接口

原文：[group__can__controller](https://docs.zephyrproject.org/latest/doxygen/html/group__can__controller.html)。读取日期：2026-10-13，`latest`。

## 362.1\_范围与基本对象

本页定义控制器局域网（Controller Area Network，CAN）控制器的应用程序编程接口（Application Programming Interface，API），声明来自 `zephyr/drivers/can.h`。自 Zephyr 1.12 提供，接口版本为 1.2.0；驱动实现侧另见 [CAN 控制器后端](P369_CAN控制器后端接口.md)。

[`can_frame`](P363_CAN帧结构.md) 表示帧（Frame），[`can_filter`](P364_CAN过滤器结构.md) 表示接收过滤器（Filter），[`can_bus_err_cnt`](P365_CAN错误计数结构.md) 保存控制器错误计数，[`can_timing`](P366_CAN时序结构.md) 保存总线时序，[`can_state_change_callback`](P367_CAN状态变化回调结构.md) 保存状态变化回调，[`can_device_state`](P368_CAN设备状态结构.md) 为 CAN 设备类别提供专用状态扩展。

发送（Transmit，TX）与接收（Receive，RX）分别使用对应的邮箱（Mailbox）或先进先出队列（First In, First Out，FIFO）。标准标识符（Standard Identifier，ID）为 11 位，扩展标识符（Extended Identifier）为 29 位。灵活数据速率 CAN（CAN with Flexible Data-Rate，CAN FD）支持独立的数据阶段配置；经典 CAN 使用 CAN 2.0A/2.0B 帧规则。

## 362.2\_模式、帧与过滤器标志

<a id="ga0b2a1456e66f4522a30cf1400fdfced7"></a>

模式类型保存控制器配置标志：

```c
typedef uint32_t can_mode_t;
```

低 24 位保留给通用模式标志，高 8 位保留给控制器或驱动专用标志，原页相关分组为 [`CAN_MODE_FLAGS`](https://docs.zephyrproject.org/latest/doxygen/html/group__can__controller.html#CAN_MODE_FLAGS)。下列 `BIT(n)` 表示第 n 位的掩码。

CAN 总线中的显性位（Dominant Bit）与隐性位（Recessive Bit）具有不同电气优先级。确认（Acknowledgement，ACK）表示接收方确认帧；仲裁（Arbitration）决定同时竞争总线的发送者谁继续发送。

| 模式宏 | 原定义 | 含义 |
| --- | --- | --- |
| <a id="ga89cd5ea2e9d70a51bc12b100be28ca3d"></a>[`CAN_MODE_NORMAL`](https://docs.zephyrproject.org/latest/doxygen/html/group__can__controller.html#ga89cd5ea2e9d70a51bc12b100be28ca3d) | `0` | 正常模式 |
| <a id="ga891031afc77974a041accb3d0ceb21bb"></a>[`CAN_MODE_LOOPBACK`](https://docs.zephyrproject.org/latest/doxygen/html/group__can__controller.html#ga891031afc77974a041accb3d0ceb21bb) | `BIT(0)` | 回环（Loopback），接收自身发出的帧 |
| <a id="ga117d04b9118a1b3f839c557ef6b596cb"></a>[`CAN_MODE_LISTENONLY`](https://docs.zephyrproject.org/latest/doxygen/html/group__can__controller.html#ga117d04b9118a1b3f839c557ef6b596cb) | `BIT(1)` | 只监听，不允许发送显性位 |
| <a id="gabb4d99736d8386a5ab62a5e44374d13a"></a>[`CAN_MODE_FD`](https://docs.zephyrproject.org/latest/doxygen/html/group__can__controller.html#gabb4d99736d8386a5ab62a5e44374d13a) | `BIT(2)` | 允许发送和接收 CAN FD 帧 |
| <a id="ga033d7ade1966299c7e6249b945f38202"></a>[`CAN_MODE_ONE_SHOT`](https://docs.zephyrproject.org/latest/doxygen/html/group__can__controller.html#ga033d7ade1966299c7e6249b945f38202) | `BIT(3)` | 单次发送，丢失仲裁或缺少 ACK 时不重传 |
| <a id="gaf0821983174ad781e1bb63a976a18fab"></a>[`CAN_MODE_3_SAMPLES`](https://docs.zephyrproject.org/latest/doxygen/html/group__can__controller.html#gaf0821983174ad781e1bb63a976a18fab) | `BIT(4)` | 三次采样（Triple Sampling） |
| <a id="ga3d8675253125b2af2bd22f0b2cc60cdd"></a>[`CAN_MODE_MANUAL_RECOVERY`](https://docs.zephyrproject.org/latest/doxygen/html/group__can__controller.html#ga3d8675253125b2af2bd22f0b2cc60cdd) | `BIT(5)` | 进入总线关闭状态后要求手动恢复 |

数据长度码（Data Length Code，DLC）编码帧中的数据长度，CAN FD 的编码范围与实际字节数不同。

| 宏 | 原定义 | 含义 |
| --- | --- | --- |
| <a id="ga4cd8ce34887b90baeeaa6a4aa048b398"></a>[`CAN_STD_ID_MASK`](https://docs.zephyrproject.org/latest/doxygen/html/group__can__controller.html#ga4cd8ce34887b90baeeaa6a4aa048b398) | `0x7FFU` | 标准 11 位标识符掩码 |
| <a id="ga15ee71e8abcf51008925585049125986"></a>[`CAN_EXT_ID_MASK`](https://docs.zephyrproject.org/latest/doxygen/html/group__can__controller.html#ga15ee71e8abcf51008925585049125986) | `0x1FFFFFFFU` | 扩展 29 位标识符掩码 |
| <a id="gadc209a027ee700faf10461e2417bee50"></a>[`CAN_MAX_DLC`](https://docs.zephyrproject.org/latest/doxygen/html/group__can__controller.html#gadc209a027ee700faf10461e2417bee50) | `8U` | CAN 2.0A/2.0B 最大 DLC |
| <a id="gad4b7310536c7e3252c2056abe64c0333"></a>[`CANFD_MAX_DLC`](https://docs.zephyrproject.org/latest/doxygen/html/group__can__controller.html#gad4b7310536c7e3252c2056abe64c0333) | `15U` | CAN FD 最大 DLC |
| <a id="ga9ed5a06a97db2c955a7db4b6e386d5e3"></a>[`CAN_FRAME_IDE`](https://docs.zephyrproject.org/latest/doxygen/html/group__can__controller.html#ga9ed5a06a97db2c955a7db4b6e386d5e3) | `BIT(0)` | 帧使用扩展 29 位 ID |
| <a id="gaed376ef16b84cd1974255fbb26dc3d7f"></a>[`CAN_FRAME_RTR`](https://docs.zephyrproject.org/latest/doxygen/html/group__can__controller.html#gaed376ef16b84cd1974255fbb26dc3d7f) | `BIT(1)` | 远程传输请求（Remote Transmission Request，RTR）帧 |
| <a id="ga22f85e1d16b93e46200f9673abdbb589"></a>[`CAN_FRAME_FDF`](https://docs.zephyrproject.org/latest/doxygen/html/group__can__controller.html#ga22f85e1d16b93e46200f9673abdbb589) | `BIT(2)` | 帧使用 CAN FD 格式（FD Format，FDF） |
| <a id="ga1fdf15ce4a3b333488f9b630ec836d52"></a>[`CAN_FRAME_BRS`](https://docs.zephyrproject.org/latest/doxygen/html/group__can__controller.html#ga1fdf15ce4a3b333488f9b630ec836d52) | `BIT(3)` | CAN FD 波特率切换（Baud Rate Switch，BRS） |
| <a id="ga83f8b7af6eb45e43aaac355de3e69e52"></a>[`CAN_FRAME_ESI`](https://docs.zephyrproject.org/latest/doxygen/html/group__can__controller.html#ga83f8b7af6eb45e43aaac355de3e69e52) | `BIT(4)` | CAN FD 错误状态指示（Error State Indicator，ESI） |
| <a id="gafa40c165d016955ec0c856a7fd53168f"></a>[`CAN_FILTER_IDE`](https://docs.zephyrproject.org/latest/doxygen/html/group__can__controller.html#gafa40c165d016955ec0c856a7fd53168f) | `BIT(0)` | 过滤器匹配扩展 29 位 ID 帧 |

`CAN_FRAME_BRS` 和 `CAN_FRAME_ESI` 仅与 [`CAN_FRAME_FDF`](https://docs.zephyrproject.org/latest/doxygen/html/group__can__controller.html#ga22f85e1d16b93e46200f9673abdbb589) 组合时有效。ESI 表示发送节点处于错误被动（Error-Passive）状态。

## 362.3\_设备定义与接收消息队列

<a id="ga599d0695abe481411660d7af2893f4a5"></a>

`CAN_DEVICE_DT_DEFINE(node_id, init_fn, pm, data, config, level, prio, api, ...)` 类似 `DEVICE_DT_DEFINE`，但包含 CAN 专用处理。它定义实现 CAN API 的设备，可根据 Kconfig 配置项 [`CONFIG_CAN_STATS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_CAN_STATS) 生成专用设备状态容器及初始化包装函数；启用 [`CONFIG_NET_CANBUS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_CANBUS) 时还定义该设备的 CAN 总线网络接口。

`node_id` 为设备树（Devicetree）节点标识符；`init_fn` 为驱动初始化函数名；`pm` 为电源管理（Power Management，PM）资源引用，不使用时为 `NULL`；`data` 为设备私有数据指针；`config` 为本实例配置结构地址；`level`、`prio` 是 `SYS_INIT` 规定的初始化级别及级内优先级；`api` 为驱动函数表初始指针，可为 `NULL`。原展开式为：

```c
IF_ENABLED(CONFIG_NET_CANBUS, (Z_NET_CANBUS_DEVICE_DT_DEFINE(node_id))) \
Z_CAN_DEVICE_STATE_DEFINE(Z_DEVICE_DT_DEV_ID(node_id));         \
Z_CAN_INIT_FN(Z_DEVICE_DT_DEV_ID(node_id), init_fn)             \
Z_DEVICE_DEFINE(node_id, Z_DEVICE_DT_DEV_ID(node_id),           \
                DEVICE_DT_NAME(node_id),                        \
                &UTIL_CAT(Z_DEVICE_DT_DEV_ID(node_id), _init),  \
                NULL, Z_DEVICE_DT_FLAGS(node_id), pm, data,     \
                config, level, prio, api,                       \
                &(Z_DEVICE_STATE_NAME(Z_DEVICE_DT_DEV_ID(node_id)).devstate), \
                __VA_ARGS__)
```

<a id="ga20266dc5e962922144e078b85ccb8351"></a>

`CAN_DEVICE_DT_INST_DEFINE(inst, ...)` 使用 `DT_DRV_COMPAT` 对应兼容类型的实例编号；以 `DT_DRV_INST(inst)` 替代节点标识符，其余参数交给节点版本：

```c
CAN_DEVICE_DT_DEFINE(DT_DRV_INST(inst), __VA_ARGS__)
```

<a id="ga7af0acdfbdad07fc3eba4cbd29bc090b"></a>

`CAN_MSGQ_DEFINE(name, max_frames)` 静态定义并初始化接收消息队列（Message Queue）。`name` 是队列名称，`max_frames` 为最多容纳的 CAN 帧数；队列的环形缓冲区（Ring Buffer）可保存这么多帧，相关使用接口为 [`can_add_rx_filter_msgq`](https://docs.zephyrproject.org/latest/doxygen/html/group__can__controller.html#gaaac20a068b7f32d2f38d1601d588b35c)：

```c
K_MSGQ_DEFINE_TYPE(name, struct can_frame, max_frames)
```

## 362.4\_错误统计递增与复位宏

本节所有宏都只在启用 [`CONFIG_CAN_STATS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_CAN_STATS) 时可用，参数 `dev_` 指向驱动实例设备结构。[`STATS_INC`](https://docs.zephyrproject.org/latest/doxygen/html/group__stats__apis.html#ga725e1bf6b2c486de9603954974d6315a) 递增由 `Z_CAN_GET_STATS` 取得的对应统计项，以下保留全部原展开式。

<a id="ga15f7ca18badbbe2fe24be68cacce6171"></a>

`CAN_STATS_ACK_ERROR_INC(dev_)` 在 ACK 槽未监测到显性位时递增确认错误计数：

```c
STATS_INC(Z_CAN_GET_STATS(dev_), ack_error)
```

<a id="ga120a37d5ae5064dcbf116e488f733764"></a>

`CAN_STATS_BIT0_ERROR_INC(dev_)` 在无法发送显性位时递增 bit0 错误，同时自动递增总位错误计数：

```c
do {                                                    \
        STATS_INC(Z_CAN_GET_STATS(dev_), bit0_error);   \
        CAN_STATS_BIT_ERROR_INC(dev_);                  \
} while (0)
```

<a id="ga678b74039632302efcb5ef80f0e3a90b"></a>

`CAN_STATS_BIT1_ERROR_INC(dev_)` 在无法发送隐性位时递增 bit1 错误，同时自动递增总位错误计数：

```c
do {                                                    \
        STATS_INC(Z_CAN_GET_STATS(dev_), bit1_error);   \
        CAN_STATS_BIT_ERROR_INC(dev_);                  \
} while (0)
```

<a id="gaf6f7efa9d99f44af6f58352f558d7fec"></a>

`CAN_STATS_BIT_ERROR_INC(dev_)` 记录无法发送显性或隐性位的错误。仅当控制器无法区分两种失败时直接调用；能够区分时，应调用 bit0 或 bit1 宏，由它们同时更新总数：

```c
STATS_INC(Z_CAN_GET_STATS(dev_), bit_error)
```

<a id="ga125ce05d40881476f5f156ad5e28c664"></a>

`CAN_STATS_CRC_ERROR_INC(dev_)` 在检测到帧的循环冗余校验（Cyclic Redundancy Check，CRC）无效时递增：

```c
STATS_INC(Z_CAN_GET_STATS(dev_), crc_error)
```

<a id="gac5809b3f5e1a463822e76921cddc9909"></a>

`CAN_STATS_FORM_ERROR_INC(dev_)` 在固定格式位域出现非法位时递增格式错误（Form Error）计数：

```c
STATS_INC(Z_CAN_GET_STATS(dev_), form_error)
```

<a id="ga06a9058924901e2d960858fb9e3a4a02"></a>

`CAN_STATS_RESET(dev_)` 将所有统计清零；驱动负责在启动控制器前执行复位：

```c
stats_reset(&(Z_CAN_GET_STATS(dev_).s_hdr))
```

<a id="ga95fe455780b38c7202b48bc6004e6f4d"></a>

`CAN_STATS_RX_OVERRUN_INC(dev_)` 在收到匹配已安装过滤器的帧、却没有存储容量时递增接收溢出（RX Overrun）计数，原因可以是接收邮箱已满或接收 FIFO 已满：

```c
STATS_INC(Z_CAN_GET_STATS(dev_), rx_overrun)
```

<a id="gae4146843944b7ffb1c96636e889282f7"></a>

`CAN_STATS_STUFF_ERROR_INC(dev_)` 在检测到位填充错误（Bit Stuffing Error）时递增：

```c
STATS_INC(Z_CAN_GET_STATS(dev_), stuff_error)
```

## 362.5\_回调类型与控制器状态

<a id="gab3675297d3e528bf19e2072f6a84bfca"></a>

<a id="gaab9525fafab78c0da0a78a2dae39bd6f"></a>

<a id="ga002ff7ba1f5be374510a902459dd9d3d"></a>

<a id="ga1dc18f69fe06a1d919b13f929100fa85"></a>

回调（Callback）的签名如下。所有 `dev` 都指向驱动实例设备结构：

```c
typedef void (*can_tx_callback_t)(const struct device *dev, int error,
                                 void *user_data);
typedef void (*can_rx_callback_t)(const struct device *dev,
                                 struct can_frame *frame, void *user_data);
typedef void (*can_state_change_callback_t)(const struct device *dev,
                                            enum can_state state,
                                            struct can_bus_err_cnt err_cnt,
                                            void *user_data);
typedef void (*can_state_change_callback_handler_t)(const struct device *dev,
                                                    struct can_state_change_callback *callback,
                                                    enum can_state state,
                                                    struct can_bus_err_cnt err_cnt);
```

发送回调的 `error` 表示发送结果，取值见后文 [`can_send`](https://docs.zephyrproject.org/latest/doxygen/html/group__can__controller.html#ga446ee31913699de3c80be05d837b5fd5)；`user_data` 是发送时提供的数据。接收回调的 `frame` 是收到的帧，`user_data` 是添加过滤器时提供的数据。状态变化回调的 [`state`](https://docs.zephyrproject.org/latest/doxygen/html/parser__state_8h.html#adc6e5733fc3c22f0a7b2914188c49c90) 为控制器状态，`err_cnt` 为错误计数值；旧式回调携带设置时的 `user_data`，结构式处理函数携带 `callback` 结构指针。

<a id="gac7ec472c26c564dd7067c49f67c8d2f7"></a>

[`can_state`](https://docs.zephyrproject.org/latest/doxygen/html/group__can__controller.html#gac7ec472c26c564dd7067c49f67c8d2f7) 枚举原文列出的状态及阈值如下，枚举没有显式赋值：

| 枚举项 | 原文状态说明 |
| --- | --- |
| <a id="ggac7ec472c26c564dd7067c49f67c8d2f7a026154ef3a7f9cb633e43ab7e63d769c"></a>[`CAN_STATE_ERROR_ACTIVE`](https://docs.zephyrproject.org/latest/doxygen/html/group__can__controller.html#ggac7ec472c26c564dd7067c49f67c8d2f7a026154ef3a7f9cb633e43ab7e63d769c) | 错误主动（Error-Active），RX/TX 错误计数小于 96 |
| <a id="ggac7ec472c26c564dd7067c49f67c8d2f7a15263a89961afbc4e813c7ccfc59e5ff"></a>[`CAN_STATE_ERROR_WARNING`](https://docs.zephyrproject.org/latest/doxygen/html/group__can__controller.html#ggac7ec472c26c564dd7067c49f67c8d2f7a15263a89961afbc4e813c7ccfc59e5ff) | 错误警告（Error-Warning），RX/TX 错误计数小于 128 |
| <a id="ggac7ec472c26c564dd7067c49f67c8d2f7ac2cd08cde738273c5e5df8306c48d8ae"></a>[`CAN_STATE_ERROR_PASSIVE`](https://docs.zephyrproject.org/latest/doxygen/html/group__can__controller.html#ggac7ec472c26c564dd7067c49f67c8d2f7ac2cd08cde738273c5e5df8306c48d8ae) | 错误被动（Error-Passive），RX/TX 错误计数小于 256 |
| <a id="ggac7ec472c26c564dd7067c49f67c8d2f7a679935a8710667fcb99423d217cd9959"></a>[`CAN_STATE_BUS_OFF`](https://docs.zephyrproject.org/latest/doxygen/html/group__can__controller.html#ggac7ec472c26c564dd7067c49f67c8d2f7a679935a8710667fcb99423d217cd9959) | 总线关闭（Bus-Off），RX/TX 错误计数大于或等于 256 |
| <a id="ggac7ec472c26c564dd7067c49f67c8d2f7a644e7a441f2e607b93528d3128508cc8"></a>[`CAN_STATE_STOPPED`](https://docs.zephyrproject.org/latest/doxygen/html/group__can__controller.html#ggac7ec472c26c564dd7067c49f67c8d2f7a644e7a441f2e607b93528d3128508cc8) | 控制器已停止，不参与 CAN 通信 |

> 译注：阈值描述中的 `RX/TX` 和大小关系按原生成页面保留；该表是页面对驱动状态的说明，不应替代硬件手册的完整错误状态机判定规则。

## 362.6\_时钟、速率范围与时序范围

本节 `dev` 为驱动实例。核心时钟查询将频率写入 `rate`，单位为赫兹（Hertz，Hz）：

```c
int can_get_core_clock(const struct device *dev, uint32_t *rate);
uint32_t can_get_bitrate_min(const struct device *dev);
uint32_t can_get_bitrate_max(const struct device *dev);
const struct can_timing *can_get_timing_min(const struct device *dev);
const struct can_timing *can_get_timing_max(const struct device *dev);
const struct can_timing *can_get_timing_data_min(const struct device *dev);
const struct can_timing *can_get_timing_data_max(const struct device *dev);
```

<a id="ga4af6d0d9ab72b195909f511ac65cb8fa"></a>

[`can_get_core_clock`](https://docs.zephyrproject.org/latest/doxygen/html/group__can__controller.html#ga4af6d0d9ab72b195909f511ac65cb8fa) 成功返回 0，失败返回负错误码。一个最小时间量子（Minimum Time Quantum，mtq）等于核心时钟频率的倒数；再经 [`can_timing`](P366_CAN时序结构.md) 中的预分频器（Prescaler）分频后，得到时间量子（Time Quantum，tq）。

<a id="ga343456749eec6144a91bacae0d94b114"></a>

<a id="ga1e6dc8026e4d922bce4d398d9f32a457"></a>

[`can_get_bitrate_min`](https://docs.zephyrproject.org/latest/doxygen/html/group__can__controller.html#ga343456749eec6144a91bacae0d94b114) / [`can_get_bitrate_max`](https://docs.zephyrproject.org/latest/doxygen/html/group__can__controller.html#ga1e6dc8026e4d922bce4d398d9f32a457) 返回控制器与收发器组合支持的最低/最高比特率（Bitrate），单位为 bit/s；最低值为 0 表示未指定下限。这些数值只表示组合的限制，能否实际达到还取决于核心时钟以及最小/最大时序参数。应同时参照时钟和相应的普通/数据阶段时序界限。

<a id="ga5a57627de4764f0bd3b4bafe07f56e6f"></a>

<a id="gabe385d0f003b1e990c78ef7a2a3f9616"></a>

<a id="ga6399ef0cefdab3da738136f8a5c59c2f"></a>

<a id="ga47a2f6d6b42121b390aa92160c833b80"></a>

[`can_get_timing_min`](https://docs.zephyrproject.org/latest/doxygen/html/group__can__controller.html#ga5a57627de4764f0bd3b4bafe07f56e6f) / [`can_get_timing_max`](https://docs.zephyrproject.org/latest/doxygen/html/group__can__controller.html#gabe385d0f003b1e990c78ef7a2a3f9616) 返回最小/最大支持时序参数的指针。数据阶段（Data Phase）版本 [`can_get_timing_data_min`](https://docs.zephyrproject.org/latest/doxygen/html/group__can__controller.html#ga6399ef0cefdab3da738136f8a5c59c2f) / [`can_get_timing_data_max`](https://docs.zephyrproject.org/latest/doxygen/html/group__can__controller.html#ga47a2f6d6b42121b390aa92160c833b80) 使用数据阶段的界限，要求启用 Kconfig 配置项 [`CONFIG_CAN_FD_MODE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_CAN_FD_MODE)；驱动未实现 CAN FD 时返回 `NULL`。

## 362.7\_计算时序

<a id="gac27fe64142603f0d32d422594356b2d7"></a>

时序计算接口使用目标比特率和采样点（Sample Point）求得结果：

```c
int can_calc_timing(const struct device *dev, struct can_timing *res,
                    uint32_t bitrate, uint16_t sample_pnt);
int can_calc_timing_data(const struct device *dev, struct can_timing *res,
                         uint32_t bitrate, uint16_t sample_pnt);
```

`res` 是结果输出结构，`bitrate` 单位为 bit/s，`sample_pnt` 是采样点占完整位时间的千分比（Permille），0 表示自动选择。比特率必须完全匹配；采样点可能无法精确匹配，算法会寻找最佳结果。对给定参数无法求解时，原文说明返回 `-EINVAL`。

自动采样点按速率选择：大于 800 kbit/s 时为 75.0%，否则大于 500 kbit/s 时为 80.0%，其余为 87.5%。成功返回 0 或正的采样点误差；`-EINVAL` 表示目标比特率或采样点越界，`-ENOTSUP` 表示不支持该比特率，`-EIO` 表示 `can_get_core_clock` 不可用。

<a id="ga358cd73ed59c2099f4b2c6ceb397ca11"></a>

[`can_calc_timing_data`](https://docs.zephyrproject.org/latest/doxygen/html/group__can__controller.html#ga358cd73ed59c2099f4b2c6ceb397ca11) 使用数据阶段的最小/最大值，其他计算规则相同；其 `bitrate` 和 `sample_pnt` 针对数据阶段，要求启用 Kconfig 配置项 [`CONFIG_CAN_FD_MODE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_CAN_FD_MODE)，返回值和错误码同上。

## 362.8\_设置时序和比特率

<a id="ga606cf9fda4c66a0f4abf74e1d357eac2"></a>

<a id="ga1b134af5d6286ea0fee130b6da5217da"></a>

直接设置时序的两个接口为：

```c
int can_set_timing(const struct device *dev, const struct can_timing *timing);
int can_set_timing_data(const struct device *dev,
                        const struct can_timing *timing_data);
int can_set_bitrate(const struct device *dev, uint32_t bitrate);
int can_set_bitrate_data(const struct device *dev, uint32_t bitrate_data);
```

`timing` 为总线时序，`timing_data` 为 CAN FD 数据阶段时序。两者成功返回 0；控制器未停止返回 `-EBUSY`，驱动不支持该时序返回 `-ENOTSUP`，配置失败的一般输入输出错误返回 `-EIO`。数据阶段函数需要 [`CONFIG_CAN_FD_MODE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_CAN_FD_MODE)，驱动未实现 CAN FD 时还可返回 `-ENOSYS`。

<a id="ga0afd2c446fc5e685370641a1678f87b7"></a>

<a id="ga0685ebfacfb79d33131167ac3aaa6f9b"></a>

[`can_set_bitrate`](https://docs.zephyrproject.org/latest/doxygen/html/group__can__controller.html#ga0685ebfacfb79d33131167ac3aaa6f9b) 的 `bitrate` 指定仲裁阶段（Arbitration Phase）比特率；[`can_set_bitrate_data`](https://docs.zephyrproject.org/latest/doxygen/html/group__can__controller.html#ga0afd2c446fc5e685370641a1678f87b7) 的 `bitrate_data` 指定数据阶段比特率，后者同样需要 [`CONFIG_CAN_FD_MODE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_CAN_FD_MODE)。

原文引用 CAN in Automation（CiA）301 v4.2.0，指出它建议所有速率均使用 87.5% 采样点，但部分控制器在高比特率时难以实现。两函数采用与 Linux 内核一致的默认位置：大于 800 kbit/s 为 75.0%，否则大于 500 kbit/s 为 80.0%，其他为 87.5%。

这两个速率函数成功返回 0；`-EBUSY` 为控制器未停止，`-EINVAL` 为目标速率越界，`-ENOTSUP` 为控制器/收发器组合不支持，`-ERANGE` 为结果采样点偏差超过 ±5%，`-EIO` 为设置失败的一般输入输出错误。

## 362.9\_能力、工作模式、收发器与启停

能力、模式与收发器查询如下：

```c
int can_get_capabilities(const struct device *dev, can_mode_t *cap);
int can_set_mode(const struct device *dev, can_mode_t mode);
can_mode_t can_get_mode(const struct device *dev);
const struct device *can_get_transceiver(const struct device *dev);
int can_start(const struct device *dev);
int can_stop(const struct device *dev);
```

<a id="ga4afd7776c5039dec8acb089499dc1168"></a>

[`can_get_capabilities`](https://docs.zephyrproject.org/latest/doxygen/html/group__can__controller.html#ga4afd7776c5039dec8acb089499dc1168) 把支持的模式写入 `cap`，成功返回 0、失败返回 `-EIO`。列出的能力不一定能同时启用，例如可能分别支持回环与只监听，却不支持组合。

<a id="gae04c3c884b3ed26dfea4745b7dff2c5f"></a>

<a id="gabd201b5b1fca54048985a8a24dd51e55"></a>

[`can_set_mode`](https://docs.zephyrproject.org/latest/doxygen/html/group__can__controller.html#gae04c3c884b3ed26dfea4745b7dff2c5f) 设置 `mode`，成功返回 0；未停止返回 `-EBUSY`，配置失败返回 `-EIO`，不支持该模式返回 `-ENOTSUP`。[`can_get_mode`](https://docs.zephyrproject.org/latest/doxygen/html/group__can__controller.html#gabd201b5b1fca54048985a8a24dd51e55) 返回当前模式。

<a id="gae012d26711c2a7ce1419d21c38cae63a"></a>

[`can_get_transceiver`](https://docs.zephyrproject.org/latest/doxygen/html/group__can__controller.html#gae012d26711c2a7ce1419d21c38cae63a) 返回关联 CAN 收发器驱动实例的设备指针，没有关联收发器则为 `NULL`。

<a id="gae48dfa8bc5b52f233b9b1a08aac2675a"></a>

[`can_start`](https://docs.zephyrproject.org/latest/doxygen/html/group__can__controller.html#gae48dfa8bc5b52f233b9b1a08aac2675a) 使控制器离开 [`CAN_STATE_STOPPED`](https://docs.zephyrproject.org/latest/doxygen/html/group__can__controller.html#ggac7ec472c26c564dd7067c49f67c8d2f7a644e7a441f2e607b93528d3128508cc8)，复位 RX/TX 错误计数，允许参与总线通信，并在支持时启用收发器；启动还会复位全部控制器统计。成功返回 0，已经启动返回 `-EALREADY`，启动失败返回 `-EIO`，相关接口为 `can_transceiver_enable`。

<a id="ga1b0ac9185341cb0bde85ec64e4c490a5"></a>

[`can_stop`](https://docs.zephyrproject.org/latest/doxygen/html/group__can__controller.html#ga1b0ac9185341cb0bde85ec64e4c490a5) 进入 [`CAN_STATE_STOPPED`](https://docs.zephyrproject.org/latest/doxygen/html/group__can__controller.html#ggac7ec472c26c564dd7067c49f67c8d2f7a644e7a441f2e607b93528d3128508cc8)，禁止参与通信，中止所有待发帧，并在支持时禁用收发器。成功返回 0，已经停止返回 `-EALREADY`，停止失败返回 `-EIO`，相关接口为 `can_transceiver_disable`。

## 362.10\_发送帧及其优先级

<a id="ga446ee31913699de3c80be05d837b5fd5"></a>

发送函数将帧排队，并可指定等待时间与完成回调：

```c
int can_send(const struct device *dev, const struct can_frame *frame,
              k_timeout_t timeout, can_tx_callback_t callback, void *user_data);
```

排队帧按优先级发送：CAN ID 越小优先级越高；ID 相同时数据帧高于 RTR 帧；基本 ID 相同，即扩展 ID 的高 11 位与标准 ID 相同时，标准帧高于扩展帧。优先级完全相同的帧，其发送顺序由硬件决定。

如果分段消息使用多个相同 ID 的帧，而且必须按 FIFO 顺序发送，发送者必须一次只排队一帧。默认情况下，控制器会在仲裁失败或缺少确认时自动重试；有些控制器可用 [`CAN_MODE_ONE_SHOT`](https://docs.zephyrproject.org/latest/doxygen/html/group__can__controller.html#ga033d7ade1966299c7e6249b945f38202) 禁用重传。

`frame` 为待发帧，`timeout` 是等待空闲发送邮箱的超时或 [`K_FOREVER`](../timer_reference/P086_系统时钟公共接口.md)（永久等待）；`callback` 在帧发出或出现发送错误时调用，`user_data` 转交给它。回调为 `NULL` 时，函数阻塞直到帧发出；从用户模式（User Mode）调用时回调必须为 `NULL`。

| 返回值 | 含义 |
| --- | --- |
| 0 | 成功 |
| `-EINVAL` | 参数无效 |
| `-ENOTSUP` | 参数不支持 |
| `-ENETDOWN` | 控制器处于停止状态 |
| `-ENETUNREACH` | 控制器处于 Bus-Off |
| `-EBUSY` | 仲裁失败，仅禁用自动重传时适用 |
| `-EIO` | 一般发送错误，例如禁用自动重传时缺少 ACK |
| `-EAGAIN` | 超时 |

## 362.11\_接收过滤器、回调与消息队列

回调接收和消息队列接收接口如下：

```c
int can_add_rx_filter(const struct device *dev, can_rx_callback_t callback,
                       void *user_data, const struct can_filter *filter);
int can_add_rx_filter_msgq(const struct device *dev, struct k_msgq *msgq,
                            const struct can_filter *filter);
void can_remove_rx_filter(const struct device *dev, int filter_id);
int can_get_max_filters(const struct device *dev, bool ide);
```

<a id="gae9dd69a13b960f773ab07bb0bb13b5e9"></a>

[`can_add_rx_filter`](https://docs.zephyrproject.org/latest/doxygen/html/group__can__controller.html#gae9dd69a13b960f773ab07bb0bb13b5e9) 为 `filter` 指定的 CAN 标识符添加回调。控制器收到匹配帧时，在中断上下文调用 `callback` 并传入 `user_data`。若一帧匹配多个过滤器，即 ID/掩码或标志重叠，匹配优先级由硬件决定；同一个回调可以用于多个过滤器。

<a id="gaaac20a068b7f32d2f38d1601d588b35c"></a>

`can_add_rx_filter_msgq` 是前者的包装，把匹配帧写入 `msgq`，从而让应用通过消息队列接收。重叠匹配的硬件优先级规则相同，同一个队列也可用于多个过滤器。

**消息队列要求：**调用前必须初始化队列，调用者必须拥有相应权限，消息大小必须等于 `sizeof(struct can_frame)`；可使用 [`CAN_MSGQ_DEFINE`](https://docs.zephyrproject.org/latest/doxygen/html/group__can__controller.html#ga7af0acdfbdad07fc3eba4cbd29bc090b) 正确定义。

**生命周期警告：**只要过滤器仍安装着，驱动就会保留队列指针。队列必须一直有效，直到通过 [`can_remove_rx_filter`](https://docs.zephyrproject.org/latest/doxygen/html/group__can__controller.html#ga822aa3142ea01582d5cfb8b478fb2847) 移除过滤器，否则收到的帧会写入已释放内存。应使用 `CAN_MSGQ_DEFINE` 静态定义队列。不得使用 `k_object_alloc` 分配的队列，因为最后一个持有权限的线程释放权限或终止时，此类对象会被释放；用户模式调用本函数时会拒绝这种队列。

消息队列溢出会被静默忽略，溢出的帧被丢弃。需要自定义错误处理时，直接组合 `can_add_rx_filter` 和 `k_msgq_put`。

两个添加函数成功都返回 `filter_id`；`-ENOSPC` 表示无空闲过滤器，`-EINVAL` 表示过滤器类型无效，`-ENOTSUP` 表示类型不支持，`-EIO` 表示添加失败的一般输入输出错误。消息队列版本还在消息大小不等于 `sizeof(struct can_frame)` 时返回 `-EINVAL`。

<a id="ga822aa3142ea01582d5cfb8b478fb2847"></a>

<a id="ga526c08539094486f07dc52aad8ed0dcc"></a>

`can_remove_rx_filter` 使用两种添加函数返回的 `filter_id` 移除过滤器，无返回值。[`can_get_max_filters`](https://docs.zephyrproject.org/latest/doxygen/html/group__can__controller.html#ga526c08539094486f07dc52aad8ed0dcc) 查询最大同时安装数量：`ide=false` 查询标准 11 位 ID，`ide=true` 查询扩展 29 位 ID；成功返回最大数量，`-EIO` 为一般输入输出错误，`-ENOSYS` 为驱动未实现。

## 362.12\_状态查询、变化通知与恢复

状态读取与回调管理接口如下：

```c
int can_get_state(const struct device *dev, enum can_state *state,
                   struct can_bus_err_cnt *err_cnt);
void can_set_state_change_callback(const struct device *dev,
                                    can_state_change_callback_t callback,
                                    void *user_data);
void can_init_state_change_callback(struct can_state_change_callback *callback,
                                     can_state_change_callback_handler_t handler);
int can_add_state_change_callback(const struct device *dev,
                                   struct can_state_change_callback *callback);
int can_remove_state_change_callback(const struct device *dev,
                                      struct can_state_change_callback *callback);
int can_recover(const struct device *dev, k_timeout_t timeout);
```

<a id="gab98c121578c8349d9dfb41d60f356857"></a>

[`can_get_state`](https://docs.zephyrproject.org/latest/doxygen/html/group__can__controller.html#gab98c121578c8349d9dfb41d60f356857) 获取当前状态，并可选获取错误计数；输出 [`state`](https://docs.zephyrproject.org/latest/doxygen/html/parser__state_8h.html#adc6e5733fc3c22f0a7b2914188c49c90)、`err_cnt` 都允许为 `NULL`。成功返回 0，获取失败返回 `-EIO`。

<a id="gacda2bc21fa0cbd7b3406dd096827923c"></a>

[`can_set_state_change_callback`](https://docs.zephyrproject.org/latest/doxygen/html/group__can__controller.html#gacda2bc21fa0cbd7b3406dd096827923c) 设置在中断上下文执行的状态变化回调；每个控制器只能注册一个，再次调用会覆盖前一个。`user_data` 传给回调。此函数已弃用，改用添加/移除接口。

<a id="gabf813d9f21982f674b213708adee9e96"></a>

<a id="gace0dd2797a133bd293d34a9ac5348e2a"></a>

<a id="ga5c1c7633e020aec2936a6ce3ba68b256"></a>

[`can_init_state_change_callback`](https://docs.zephyrproject.org/latest/doxygen/html/group__can__controller.html#gabf813d9f21982f674b213708adee9e96) 为 `static inline`，使用处理函数 `handler` 初始化 `callback` 结构。[`can_add_state_change_callback`](https://docs.zephyrproject.org/latest/doxygen/html/group__can__controller.html#gace0dd2797a133bd293d34a9ac5348e2a) 注册该结构，处理函数同样在中断上下文执行；成功返回 0，失败返回负错误码。[`can_remove_state_change_callback`](https://docs.zephyrproject.org/latest/doxygen/html/group__can__controller.html#ga5c1c7633e020aec2936a6ce3ba68b256) 移除指定结构，成功返回 0，失败返回负错误码，其中 `-EINVAL` 表示未找到该回调。

<a id="gac474e56a50685736a1c25dca277aab5e"></a>

[`can_recover`](https://docs.zephyrproject.org/latest/doxygen/html/group__can__controller.html#gac474e56a50685736a1c25dca277aab5e) 将控制器从 Bus-Off 恢复到 Error-Active，要求启用 Kconfig 配置项 [`CONFIG_CAN_MANUAL_RECOVERY_MODE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_CAN_MANUAL_RECOVERY_MODE)。`timeout` 是等待恢复的超时或 [`K_FOREVER`](../timer_reference/P086_系统时钟公共接口.md)。成功返回 0；`-ENOTSUP` 为未处于手动恢复模式，`-ENETDOWN` 为控制器已停止，`-EAGAIN` 为超时，`-ENOSYS` 为驱动未实现，`-EIO` 为恢复失败的一般输入输出错误。

## 362.13\_读取错误统计

以下函数只在启用 [`CONFIG_CAN_STATS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_CAN_STATS) 时可用，参数 `dev` 为驱动实例，返回对应的无符号 32 位统计计数：

```c
uint32_t can_stats_get_bit_errors(const struct device *dev);
uint32_t can_stats_get_bit0_errors(const struct device *dev);
uint32_t can_stats_get_bit1_errors(const struct device *dev);
uint32_t can_stats_get_stuff_errors(const struct device *dev);
uint32_t can_stats_get_crc_errors(const struct device *dev);
uint32_t can_stats_get_form_errors(const struct device *dev);
uint32_t can_stats_get_ack_errors(const struct device *dev);
uint32_t can_stats_get_rx_overruns(const struct device *dev);
```

<a id="ga27b277f3b5146590f159171f602904db"></a>

<a id="ga7c380f6c4a529e5b5e6010ab4e6c7680"></a>

<a id="ga4c7d40951a2ae6eaa72e5d1f7a26ac75"></a>

[`can_stats_get_bit_errors`](https://docs.zephyrproject.org/latest/doxygen/html/group__can__controller.html#ga27b277f3b5146590f159171f602904db) 读取无法发送显性或隐性位的总错误计数；[`can_stats_get_bit0_errors`](https://docs.zephyrproject.org/latest/doxygen/html/group__can__controller.html#ga7c380f6c4a529e5b5e6010ab4e6c7680) 读取显性位发送失败计数，[`can_stats_get_bit1_errors`](https://docs.zephyrproject.org/latest/doxygen/html/group__can__controller.html#ga4c7d40951a2ae6eaa72e5d1f7a26ac75) 读取隐性位发送失败计数。

<a id="ga162fde4e622fb06dcbbcf2f31bb35d38"></a>

<a id="ga31692aef7962172532f8200fed7aecd2"></a>

<a id="gabf9ce221f4f6a8dbaafcff9b7a5c5a10"></a>

<a id="ga4f8414d64b75d4d1ffb7a0feff36f698"></a>

[`can_stats_get_stuff_errors`](https://docs.zephyrproject.org/latest/doxygen/html/group__can__controller.html#ga162fde4e622fb06dcbbcf2f31bb35d38) 读取位填充错误计数；[`can_stats_get_crc_errors`](https://docs.zephyrproject.org/latest/doxygen/html/group__can__controller.html#ga31692aef7962172532f8200fed7aecd2) 读取帧 CRC 无效计数；[`can_stats_get_form_errors`](https://docs.zephyrproject.org/latest/doxygen/html/group__can__controller.html#gabf9ce221f4f6a8dbaafcff9b7a5c5a10) 读取固定格式位域中存在非法位的错误计数；[`can_stats_get_ack_errors`](https://docs.zephyrproject.org/latest/doxygen/html/group__can__controller.html#ga4f8414d64b75d4d1ffb7a0feff36f698) 读取 ACK 槽中未观察到显性位的错误计数。

<a id="ga8664fbaa13f4bb89540493264d2a041d"></a>

[`can_stats_get_rx_overruns`](https://docs.zephyrproject.org/latest/doxygen/html/group__can__controller.html#ga8664fbaa13f4bb89540493264d2a041d) 读取接收溢出计数，即收到匹配已安装过滤器的帧，却因接收邮箱或 FIFO 已满而无法保存的次数。

## 362.14\_长度转换与过滤匹配工具

三个 `static inline` 工具函数如下：

```c
uint8_t can_dlc_to_bytes(uint8_t dlc);
uint8_t can_bytes_to_dlc(uint8_t num_bytes);
bool can_frame_matches_filter(const struct can_frame *frame,
                               const struct can_filter *filter);
```

<a id="gaa1d866167c0c23f8d5c0c15385589601"></a>

<a id="ga8314716fe2b66d567b3fd377b8ee9dc3"></a>

[`can_dlc_to_bytes`](https://docs.zephyrproject.org/latest/doxygen/html/group__can__controller.html#gaa1d866167c0c23f8d5c0c15385589601) 把 `dlc` 数据长度码转换为字节数；[`can_bytes_to_dlc`](https://docs.zephyrproject.org/latest/doxygen/html/group__can__controller.html#ga8314716fe2b66d567b3fd377b8ee9dc3) 把 `num_bytes` 字节数转换为数据长度码。

<a id="gaafc54ac799e3a3a098a9f6941d7f2ea8"></a>

[`can_frame_matches_filter`](https://docs.zephyrproject.org/latest/doxygen/html/group__can__controller.html#gaafc54ac799e3a3a098a9f6941d7f2ea8) 检查 CAN 帧 `frame` 是否匹配过滤器 `filter`，匹配返回 `true`，否则返回 `false`。

---

[上一章：CAN公共接口](P361_CAN公共接口.md) · [下一章：CAN帧结构](P363_CAN帧结构.md) · [返回大纲](大纲.md)
