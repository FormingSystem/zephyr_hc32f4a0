---
id: learning.zephyr-docs.usb.page-7
title: USBC设备栈
kind: reference
status: maintained
domains: [zephyr, usb, driver]
source_url: https://docs.zephyrproject.org/latest/services/connectivity/usb/pd/ucds.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第7章\_USBC设备栈

原文：[官方页面](https://docs.zephyrproject.org/latest/services/connectivity/usb/pd/ucds.html)。读取日期：2026-10-14；保存的 latest 页面及 HTML 摘要见[来源记录](../SOURCES.md)。

## 7.1\_USB-C设备栈的职责

USB-C 设备栈在 Type-C 端口控制器（Type-C Port Controller，TCPC）与用户应用之间提供独立于硬件的接口。它移植自 Google ChromeOS 的 Type-C 端口管理器（Type-C Port Manager，TCPM）协议栈，提供以下功能：

- 使用 Type-C 端口控制器驱动提供的 API，与端口控制器交互。
- 为用户应用提供编程接口，接口定义见[include/zephyr/usb_c/usbc.h](https://github.com/zephyrproject-rtos/zephyr/blob/main/include/zephyr/usb_c/usbc.h)。

> 译注：本文围绕 USB-C 连接和 USB 电力传输（USB Power Delivery，USB PD）的策略管理。供电端（Source）向端口伙伴供电，受电端（Sink）从伙伴取电；供电角色与 USB 数据角色分别描述不同职责，不能仅凭接口外形推定它们。下文保留完整官方代码，具体端口、ADC、GPIO、电源控制设备及能力声明均属于相应官方示例。

## 7.2\_配置选项

USB-C 设备栈支持仅受电、仅供电和双电源角色（Dual Role Power，DRP）设备。

| 配置选项 | 连接状态机（Connection State Machine） |
| --- | --- |
| [`CONFIG_USBC_CSM_SINK_ONLY`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USBC_CSM_SINK_ONLY) | 受电端 USB-C 连接状态机。 |
| [`CONFIG_USBC_CSM_SOURCE_ONLY`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USBC_CSM_SOURCE_ONLY) | 供电端 USB-C 连接状态机。 |
| [`CONFIG_USBC_CSM_DRP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USBC_CSM_DRP) | 双电源角色 USB-C 连接状态机。 |

不同用途的示例见[示例列表](P009_USBC示例目录.md)。

## 7.3\_实现支持Type-C与USB PD的受电端设备

USB-C 设备需要在协议栈层和设备树（Devicetree）中进行配置。必须定义：

- 引用 TCPC 的设备树 `usb-c-connector` 节点。
- 引用 VBUS 测量设备的设备树 `vbus` 节点。
- 封装应用专用数据的自定义结构体。
- 策略回调（Policy Callback）。

下面以 USB-C Sink 示例应用为例。

### 7.3.1\_端口与VBUS测量设备

每个物理 Type-C 端口由设备树中兼容标识为 `usb-c-connector` 的节点表示：

```dts
		port1: usbc-port@1 {
			compatible = "usb-c-connector";
			reg = <1>;
			tcpc = <&ucpd1>;
			vbus = <&vbus1>;
			power-role = "sink";
			sink-pdos = <PDO_FIXED(5000, 100, 0)>;
		};
```

VBUS 由设备树中所引用的 `usb-c-vbus-adc` 兼容设备测量：

```dts
	vbus1: vbus {
		compatible = "zephyr,usb-c-vbus-adc";
		io-channels = <&adc2 8>;
		output-ohms = <49900>;
		full-ohms = <(330000 + 49900)>;
	};
```

> 译注：VBUS 为总线电源线路；上面实际的完整 `compatible` 字符串是 `zephyr,usb-c-vbus-adc`。`io-channels` 关联模数转换器（Analog-to-Digital Converter，ADC）输入；`output-ohms` 和 `full-ohms` 描述分压电阻关系。端口中的 `sink-pdos` 保存受电能力，电力数据对象（Power Data Object，PDO）表达可协商的电源条件。示例中的 `PDO_FIXED(5000, 100, 0)` 对应固定电源能力，不能把其中参数替换为未经硬件核对的数值。

### 7.3.2\_应用数据与能力回调

定义自定义结构体，稍后将其注册到子系统；回调可以通过 API 访问这个结构体。

```c
/**
 * @brief A structure that encapsulates Port data.
 */
static struct port0_data_t {
	/** Sink Capabilities */
	uint32_t snk_caps[DT_PROP_LEN(USBC_PORT0_NODE, sink_pdos)];
	/** Number of Sink Capabilities */
	int snk_cap_cnt;
	/** Source Capabilities */
	uint32_t src_caps[PDO_MAX_DATA_OBJECTS];
	/** Number of Source Capabilities */
	int src_cap_cnt;
	/* Power Supply Ready flag */
	atomic_t ps_ready;
} port0_data = {.snk_caps = DT_PROP(USBC_PORT0_NODE, sink_pdos),
		.snk_cap_cnt = DT_PROP_LEN(USBC_PORT0_NODE, sink_pdos),
		.src_caps = {0},
		.src_cap_cnt = 0,
		.ps_ready = 0};
```

子系统使用以下回调设置或取得应用专用数据：

```c
static int port0_policy_cb_get_snk_cap(const struct device *dev, uint32_t **pdos, int *num_pdos)
{
	struct port0_data_t *dpm_data = usbc_get_dpm_data(dev);

	*pdos = dpm_data->snk_caps;
	*num_pdos = dpm_data->snk_cap_cnt;

	return 0;
}

static void port0_policy_cb_set_src_cap(const struct device *dev, const uint32_t *pdos,
					const int num_pdos)
{
	struct port0_data_t *dpm_data;
	int num;
	int i;

	dpm_data = usbc_get_dpm_data(dev);

	num = num_pdos;
	if (num > PDO_MAX_DATA_OBJECTS) {
		num = PDO_MAX_DATA_OBJECTS;
	}

	for (i = 0; i < num; i++) {
		dpm_data->src_caps[i] = *(pdos + i);
	}

	dpm_data->src_cap_cnt = num;
}

static uint32_t port0_policy_cb_get_rdo(const struct device *dev)
{
	struct port0_data_t *dpm_data = usbc_get_dpm_data(dev);

	return build_rdo(dpm_data);
}
```

> 译注：`snk_caps`／`snk_cap_cnt` 保存本端受电能力，`src_caps`／`src_cap_cnt` 保存伙伴供电能力。`usbc_get_dpm_data()` 取回应用注册的设备策略管理器（Device Policy Manager，DPM）数据；接收能力列表时最多保存 `PDO_MAX_DATA_OBJECTS` 项。请求数据对象（Request Data Object，RDO）由示例的 `build_rdo()` 根据应用策略构造，这个辅助函数并未在上述摘录中展开。

### 7.3.3\_策略检查与事件通知

子系统通过以下回调询问某项操作是否允许执行：

```c
bool port0_policy_check(const struct device *dev, const enum usbc_policy_check_t policy_check)
{
	switch (policy_check) {
	case CHECK_POWER_ROLE_SWAP:
		/* Reject power role swaps */
		return false;
	case CHECK_DATA_ROLE_SWAP_TO_DFP:
		/* Reject data role swap to DFP */
		return false;
	case CHECK_DATA_ROLE_SWAP_TO_UFP:
		/* Accept data role swap to UFP */
		return true;
	case CHECK_SNK_AT_DEFAULT_LEVEL:
		/* This device is always at the default power level */
		return true;
	default:
		/* Reject all other policy checks */
		return false;
	}
}
```

> 译注：该受电端示例拒绝供电角色交换和切换到面向下游端口（Downstream Facing Port，DFP），允许切换到面向上游端口（Upstream Facing Port，UFP），并报告自身一直处于默认供电级别；其他策略查询返回 `false`。这是样例策略，不是全部应用必须采用的策略。

子系统通过以下回调向应用通知事件：

```c
static void port0_notify(const struct device *dev, const enum usbc_policy_notify_t policy_notify)
{
	struct port0_data_t *dpm_data = usbc_get_dpm_data(dev);

	switch (policy_notify) {
	case PROTOCOL_ERROR:
		break;
	case MSG_DISCARDED:
		break;
	case MSG_ACCEPT_RECEIVED:
		break;
	case MSG_REJECTED_RECEIVED:
		break;
	case MSG_NOT_SUPPORTED_RECEIVED:
		break;
	case TRANSITION_PS:
		atomic_set_bit(&dpm_data->ps_ready, 0);
		break;
	case PD_CONNECTED:
		break;
	case NOT_PD_CONNECTED:
		break;
	case POWER_CHANGE_0A0:
		LOG_INF("PWR 0A");
		break;
	case POWER_CHANGE_DEF:
		LOG_INF("PWR DEF");
		break;
	case POWER_CHANGE_1A5:
		LOG_INF("PWR 1A5");
		break;
	case POWER_CHANGE_3A0:
		LOG_INF("PWR 3A0");
		break;
	case DATA_ROLE_IS_UFP:
		break;
	case DATA_ROLE_IS_DFP:
		break;
	case PORT_PARTNER_NOT_RESPONSIVE:
		LOG_INF("Port Partner not PD Capable");
		break;
	case SNK_TRANSITION_TO_DEFAULT:
		break;
	case HARD_RESET_RECEIVED:
		break;
	case SENDER_RESPONSE_TIMEOUT:
		break;
	case SOURCE_CAPABILITIES_RECEIVED:
		break;
	default:
	}
}
```

> 译注：此回调在 `TRANSITION_PS` 时设置供电就绪标志 `ps_ready`，为电流能力变化输出日志，并在伙伴不响应时报告对方不具备 PD 能力；其余列出的分支未执行应用动作。`PWR DEF` 表示默认电流能力，`PWR 1A5`／`PWR 3A0` 分别表示 1.5 A／3.0 A 能力通知。原代码末尾的空 `default:` 分支照实保留；这里是官方页面摘录，不把它声称为本批编译验证过的独立程序。

### 7.3.4\_注册并启动

注册回调：

```c
	/* Register USB-C Callbacks */

	/* Register Policy Check callback */
	usbc_set_policy_cb_check(usbc_port0, port0_policy_check);
	/* Register Policy Notify callback */
	usbc_set_policy_cb_notify(usbc_port0, port0_notify);
	/* Register Policy Get Sink Capabilities callback */
	usbc_set_policy_cb_get_snk_cap(usbc_port0, port0_policy_cb_get_snk_cap);
	/* Register Policy Set Source Capabilities callback */
	usbc_set_policy_cb_set_src_cap(usbc_port0, port0_policy_cb_set_src_cap);
	/* Register Policy Get Request Data Object callback */
	usbc_set_policy_cb_get_rdo(usbc_port0, port0_policy_cb_get_rdo);
```

注册自定义结构体：

```c
	/* Set Application port data object. This object is passed to the policy callbacks */
	port0_data.ps_ready = ATOMIC_INIT(0);
	usbc_set_dpm_data(usbc_port0, &port0_data);
```

启动 USB-C 子系统：

```c
	/* Start the USB-C Subsystem */
	usbc_start(usbc_port0);
```

> 译注：上述片段需放入完整应用上下文。当前官方 Sink 示例先由 `DT_ALIAS(usbc_port0)` 获取端口并检查 `device_is_ready()`，再注册回调与数据，最后启动子系统；主循环读取并清除 `ps_ready` 标志以显示供电能力。示例中变量的 `port0` 命名不要求设备树节点标签必须也叫 `port0`，关键在于别名所引用的节点。

## 7.4\_实现支持Type-C与USB PD的供电端设备

供电端同样需要在协议栈层和设备树中配置。定义以下节点、结构体和回调：

- 引用 TCPC 的设备树 `usb-c-connector` 节点。
- 引用 VBUS 测量设备的设备树 `vbus` 节点。
- 用于 VBUS 与 VCONN 电源控制的设备树 `pwrctrl` 节点。
- 封装应用专用数据的自定义结构体。
- 策略回调。

下面以 USB-C Source 示例应用为例。

### 7.4.1\_端口、测量与电源控制

每个物理 Type-C 端口由设备树中兼容标识为 `usb-c-connector` 的节点表示：

```dts
		port1: usbc-port@1 {
			compatible = "usb-c-connector";
			reg = <1>;
			tcpc = <&ucpd1>;
			vbus = <&vbus1>;
			power-role = "source";
			typec-power-opmode = "3.0A";
			source-pdos = <PDO_FIXED(5000, 100, 0) PDO_FIXED(9000, 100, 0)
				       PDO_FIXED(15000, 100, 0)>;
		};
```

VBUS 由设备树中所引用的 `usb-c-vbus-adc` 兼容设备测量：

```dts
	vbus1: vbus {
		compatible = "zephyr,usb-c-vbus-adc";
		io-channels = <&adc1 9>;
		output-ohms = <49900>;
		full-ohms = <(330000 + 49900)>;

		/* Pin B13 is used to control VBUS Discharge for Port1 */
		discharge-gpios = <&gpiob 13 GPIO_ACTIVE_HIGH>;
	};
```

VBUS 与 VCONN 的电源控制可交给设备树中兼容标识为 `zephyr,usb-c-pwrctrl` 的设备：

```dts
	pwrctrl1: pwrctrl {
		compatible = "zephyr,usb-c-pwrctrl";

		/* Pin D3 is used to enable VBUS Source */
		source-en-gpios = <&gpiod 3 GPIO_ACTIVE_HIGH>;

		/* Pin A1 is used for DCDC_EN */
		dcdc-en-gpios = <&gpioa 1 GPIO_ACTIVE_HIGH>;

		/* Pin D4 enables VCONN on CC1 */
		vconn1-en-gpios = <&gpiod 4 GPIO_ACTIVE_LOW>;

		/* Pin B9 enables VCONN on CC2 */
		vconn2-en-gpios = <&gpiob 9 GPIO_ACTIVE_LOW>;

		/* PWM for voltage selection */
		pwms = <&pwm15 1 PWM_USEC(50) PWM_POLARITY_INVERTED>;
	};
```

> 译注：VCONN 为线缆相关电路提供电源，与 VBUS 不同。原示例用 GPIO 控制 VBUS 供电、放电、DC-DC 使能和两条配置通道（Configuration Channel，CC）上的 VCONN，用脉宽调制（Pulse Width Modulation，PWM）选择电压。`typec-power-opmode` 的 Type-C 电流声明和 `source-pdos` 中的 PD 能力是不同配置项，必须分别对应实际电源设计；本页不表明其他开发板具有原示例的这些引脚和电路。

### 7.4.2\_应用数据与供电策略回调

定义自定义结构体，稍后注册到子系统，回调可通过 API 取得它：

```c
/**
 * @brief A structure that encapsulates Port data.
 */
static struct port0_data_t {
	/** Power controller device */
	const struct device *pwrctrl;
	/** Source Capabilities */
	uint32_t src_caps[DT_PROP_LEN(USBC_PORT0_NODE, source_pdos)];
	/** Number of Source Capabilities */
	int src_cap_cnt;
	/** CC Rp value */
	int rp;
	/** Sink Request RDO */
	union pd_rdo sink_request;
	/** Requested Object Pos */
	int obj_pos;
	/** VCONN CC line*/
	enum tc_cc_polarity vconn_pol;
	/** True if power supply is ready */
	bool ps_ready;
	/** True if power supply should transition to a new level */
	bool ps_tran_start;
	/** Log Sink Requested RDO to console */
	atomic_t show_sink_request;
} port0_data = {
	.rp = DT_ENUM_IDX(USBC_PORT0_NODE, typec_power_opmode),
	.src_caps = DT_PROP(USBC_PORT0_NODE, source_pdos),
	.src_cap_cnt = DT_PROP_LEN(USBC_PORT0_NODE, source_pdos),
};
```

子系统通过以下回调设置或获取应用专用数据：

```c
/**
 * @brief PE calls this function when it needs to set the Rp on CC
 */
int port0_policy_cb_get_src_rp(const struct device *dev, enum tc_rp_value *rp)
{
	struct port0_data_t *dpm_data = usbc_get_dpm_data(dev);

	*rp = dpm_data->rp;

	return 0;
}

/**
 * @brief PE calls this function to Enable (5V) or Disable (0V) the
 *	  Power Supply
 */
int port0_policy_cb_src_en(const struct device *dev, bool en)
{
	struct port0_data_t *dpm_data = usbc_get_dpm_data(dev);

	source_ctrl_set(dpm_data->pwrctrl, en ? SOURCE_5V : SOURCE_0V);

	return 0;
}

/**
 * @brief PE calls this function to Enable or Disable VCONN
 */
int port0_policy_cb_vconn_en(const struct device *tcpc_dev, const struct device *usbc_dev,
			     enum tc_cc_polarity pol, bool en)
{
	struct port0_data_t *dpm_data = usbc_get_dpm_data(usbc_dev);

	dpm_data->vconn_pol = pol;

	if (en == false) {
		/* Disable VCONN on CC1 and CC2 */
		vconn_ctrl_set(dpm_data->pwrctrl, VCONN_OFF);
	} else if (pol == TC_POLARITY_CC1) {
		/* set VCONN on CC1 */
		vconn_ctrl_set(dpm_data->pwrctrl, VCONN1_ON);
	} else {
		/* set VCONN on CC2 */
		vconn_ctrl_set(dpm_data->pwrctrl, VCONN2_ON);
	}

	return 0;
}

/**
 * @brief PE calls this function to get the Source Caps that will be sent
 *	  to the Sink
 */
int port0_policy_cb_get_src_caps(const struct device *dev, const uint32_t **pdos,
				 uint32_t *num_pdos)
{
	struct port0_data_t *dpm_data = usbc_get_dpm_data(dev);

	*pdos = dpm_data->src_caps;
	*num_pdos = dpm_data->src_cap_cnt;

	return 0;
}

/**
 * @brief PE calls this function to verify that a Sink's request if valid
 */
static enum usbc_snk_req_reply_t port0_policy_cb_check_sink_request(const struct device *dev,
								    const uint32_t request_msg)
{
	struct port0_data_t *dpm_data = usbc_get_dpm_data(dev);
	union pd_fixed_supply_pdo_source pdo;
	uint32_t obj_pos;
	uint32_t op_current;

	dpm_data->sink_request.raw_value = request_msg;
	obj_pos = dpm_data->sink_request.fixed.object_pos;
	op_current =
		PD_CONVERT_FIXED_PDO_CURRENT_TO_MA(dpm_data->sink_request.fixed.operating_current);

	if (obj_pos == 0 || obj_pos > dpm_data->src_cap_cnt) {
		return SNK_REQUEST_REJECT;
	}

	pdo.raw_value = dpm_data->src_caps[obj_pos - 1];

	if (dpm_data->sink_request.fixed.operating_current > pdo.max_current) {
		return SNK_REQUEST_REJECT;
	}

	dpm_data->obj_pos = obj_pos;

	atomic_set_bit(&port0_data.show_sink_request, 0);

	/*
	 * Clear PS ready. This will be set to true after PS is ready after
	 * it transitions to the new level.
	 */
	port0_data.ps_ready = false;

	return SNK_REQUEST_VALID;
}

/**
 * @brief PE calls this function to check if the Power Supply is at the requested
 *	  level
 */
static bool port0_policy_cb_is_ps_ready(const struct device *dev)
{
	struct port0_data_t *dpm_data = usbc_get_dpm_data(dev);

	/* Return true to inform that the Power Supply is ready */
	return dpm_data->ps_ready;
}

/**
 * @brief PE calls this function to check if the Present Contract is still
 *	  valid
 */
static bool port0_policy_cb_present_contract_is_valid(const struct device *dev,
						      const uint32_t present_contract)
{
	struct port0_data_t *dpm_data = usbc_get_dpm_data(dev);
	union pd_fixed_supply_pdo_source pdo;
	union pd_rdo request;
	uint32_t obj_pos;
	uint32_t op_current;

	request.raw_value = present_contract;
	obj_pos = request.fixed.object_pos;
	op_current = PD_CONVERT_FIXED_PDO_CURRENT_TO_MA(request.fixed.operating_current);

	if (obj_pos == 0 || obj_pos > dpm_data->src_cap_cnt) {
		return false;
	}

	pdo.raw_value = dpm_data->src_caps[obj_pos - 1];

	if (request.fixed.operating_current > pdo.max_current) {
		return false;
	}

	return true;
}
```

> 译注：这些回调供策略引擎（Policy Engine，PE）使用，依次负责取得 CC 上的 Rp 值、启停 5 V 供电、控制 VCONN、取得供电能力列表、核验受电端请求、查询电源是否就绪，以及核验当前供电契约（Present Contract）是否仍然有效。请求检查先验证 PDO 对象位置，再比较工作电流与对应 PDO 的最大电流；有效请求会保存对象位置、置位显示标志，并清除就绪状态，等待电源切换完成。`source_ctrl_set()` 与 `vconn_ctrl_set()` 是完整示例提供的电源控制辅助函数，不由这些摘录单独实现。

### 7.4.3\_策略检查与事件通知

子系统使用以下回调查询是否允许执行某项操作：

```c
bool port0_policy_check(const struct device *dev, const enum usbc_policy_check_t policy_check)
{
	struct port0_data_t *dpm_data = usbc_get_dpm_data(dev);

	switch (policy_check) {
	case CHECK_POWER_ROLE_SWAP:
		/* Reject power role swaps */
		return false;
	case CHECK_DATA_ROLE_SWAP_TO_DFP:
		/* Accept data role swap to DFP */
		return true;
	case CHECK_DATA_ROLE_SWAP_TO_UFP:
		/* Reject data role swap to UFP */
		return false;
	case CHECK_SRC_PS_AT_DEFAULT_LEVEL:
		/*
		 * This check is sent from the PE_SRC_Transition_to_default
		 * state and requires the following:
		 *	1: Vconn should be turned ON
		 *	2: Return TRUE when Power Supply is at default level
		 */

		/* Power on VCONN */
		vconn_ctrl_set(dpm_data->pwrctrl, dpm_data->vconn_pol);

		/* PS should be at default level after receiving a Hard Reset */
		return true;
	default:
		/* Reject all other policy checks */
		return false;
	}
}
```

> 译注：此供电端示例拒绝供电角色交换，允许切换到 DFP、拒绝切换到 UFP。`CHECK_SRC_PS_AT_DEFAULT_LEVEL` 对应恢复默认供电级别时的检查；代码按该示例假定，在硬复位（Hard Reset）后的恢复阶段启用 VCONN 并返回就绪。其他策略检查被拒绝。

子系统使用以下回调通知应用发生的事件：

```c
static void port0_notify(const struct device *dev, const enum usbc_policy_notify_t policy_notify)
{
	struct port0_data_t *dpm_data = usbc_get_dpm_data(dev);

	switch (policy_notify) {
	case PROTOCOL_ERROR:
		break;
	case MSG_DISCARDED:
		break;
	case MSG_ACCEPT_RECEIVED:
		break;
	case MSG_REJECTED_RECEIVED:
		break;
	case MSG_NOT_SUPPORTED_RECEIVED:
		break;
	case TRANSITION_PS:
		dpm_data->ps_tran_start = true;
		break;
	case PD_CONNECTED:
		break;
	case NOT_PD_CONNECTED:
		break;
	case DATA_ROLE_IS_UFP:
		break;
	case DATA_ROLE_IS_DFP:
		break;
	case PORT_PARTNER_NOT_RESPONSIVE:
		LOG_INF("Port Partner not PD Capable");
		break;
	case HARD_RESET_RECEIVED:
		/*
		 * This notification is sent from the PE_SRC_Transition_to_default
		 * state and requires the following:
		 *	1: Vconn should be turned OFF
		 *	2: Reset of the local hardware
		 */

		/* Power off VCONN */
		vconn_ctrl_set(dpm_data->pwrctrl, VCONN_OFF);
		/* Transition PS to Default level */
		source_ctrl_set(dpm_data->pwrctrl, SOURCE_5V);
		break;
	default:
	}
}
```

> 译注：`TRANSITION_PS` 设置 `ps_tran_start`，通知主循环进行电压切换；收到硬复位时关闭 VCONN，并将 VBUS 恢复到默认 5 V。其他列出的分支按原代码处理或忽略。这里只翻译和说明官方回调，没有执行电源控制。

### 7.4.4\_注册并启动

注册回调：

```c
	/* Register USB-C Callbacks */

	/* Register Policy Check callback */
	usbc_set_policy_cb_check(usbc_port0, port0_policy_check);
	/* Register Policy Notify callback */
	usbc_set_policy_cb_notify(usbc_port0, port0_notify);
	/* Register Policy callback to set the Rp on CC lines */
	usbc_set_policy_cb_get_src_rp(usbc_port0, port0_policy_cb_get_src_rp);
	/* Register Policy callback to enable or disable power supply */
	usbc_set_policy_cb_src_en(usbc_port0, port0_policy_cb_src_en);
	/* Register Policy callback to enable or disable vconn */
	usbc_set_vconn_control_cb(usbc_port0, port0_policy_cb_vconn_en);
	/* Register Policy callback to send the source caps to the sink */
	usbc_set_policy_cb_get_src_caps(usbc_port0, port0_policy_cb_get_src_caps);
	/* Register Policy callback to check if the sink request is valid */
	usbc_set_policy_cb_check_sink_request(usbc_port0, port0_policy_cb_check_sink_request);
	/* Register Policy callback to check if the power supply is ready */
	usbc_set_policy_cb_is_ps_ready(usbc_port0, port0_policy_cb_is_ps_ready);
	/* Register Policy callback to check if Present Contract is still valid */
	usbc_set_policy_cb_present_contract_is_valid(usbc_port0,
						     port0_policy_cb_present_contract_is_valid);
```

注册自定义结构体：

```c
	/* Set Application port data object. This object is passed to the policy callbacks */
	usbc_set_dpm_data(usbc_port0, &port0_data);
```

启动 USB-C 子系统：

```c
	/* Start the USB-C Subsystem */
	usbc_start(usbc_port0);
```

> 译注：完整 Source 示例还会取得并检查端口和电源控制设备，初始化请求显示、切换与就绪标志。启动后的主循环在 `ps_tran_start` 置位时调用 `source_ctrl_set()`，完成后更新 `ps_ready`，并显示受电端请求；不能仅复制注册片段就认为应用的电压切换工作已经完整。

## 7.5\_实现双电源角色设备

DRP 设备既可作为 Source，也可作为 Sink，与端口伙伴自动协商适当角色。未连接时，设备交替在 CC 线上通告 Source（Rp）和 Sink（Rd），以检测并连接任一类型的伙伴。检测到连接后，设备进入相应的已连接状态（`Attached.SRC` 或 `Attached.SNK`），并启动对应的策略引擎状态机（`PE_SRC` 或 `PE_SNK`）协商供电。

配置方法与 Source、Sink 类似，主要区别是：

- 在设备树 `usb-c-connector` 节点中设置 `power-role = "dual"`。
- 同时实现 Source 和 Sink 操作所需的回调。

可通过 Kconfig 配置 DRP 切换行为：

| 选项 | 范围与默认值 |
| --- | --- |
| [`CONFIG_USBC_DRP_PERIOD_MS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USBC_DRP_PERIOD_MS) | 切换周期 50～100 ms，默认 75 ms。 |
| [`CONFIG_USBC_DRP_DUTY_CYCLE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USBC_DRP_DUTY_CYCLE) | 以 Source 身份通告的时间占比 30%～70%，默认 50%。 |

完整示例见[基础 USB-C DRP](P010_USBC双电源角色示例.md#usb-c-drp)。

> 译注：当前 Kconfig 将上述三种连接状态机放在一个 `choice` 中；使用 DRP 时需选中 [`CONFIG_USBC_CSM_DRP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USBC_CSM_DRP)。周期指 Source→Sink→Source 的完整切换周期，不能把默认 75 ms 解释为每个角色各停留 75 ms。未连接时的角色探测，也不同于已建立供电契约后的供电角色交换。

## 7.6\_API参考与相关示例

接口参考：[USB-C 设备 API](https://docs.zephyrproject.org/latest/doxygen/html/group____usbc__device__api.html)。

| 示例 | 作用 |
| --- | --- |
| [基础 USB-C DRP](P010_USBC双电源角色示例.md#usb-c-drp) | 实现双电源角色 USB-C PD 应用。 |
| [基础 USB-C Sink](P011_USBC受电端示例.md#usb-c-sink) | 实现受电端 USB-C PD 应用。 |
| [基础 USB-C Source](P012_USBC供电端示例.md#usb-c-source) | 实现供电端 USB-C PD 应用。 |

受电端回调参考：[Sink_callbacks](https://docs.zephyrproject.org/latest/doxygen/html/group__sink__callbacks.html)。供电端回调参考：[Source_callbacks](https://docs.zephyrproject.org/latest/doxygen/html/group__source__callbacks.html)。


译注核对来源：[include/zephyr/usb_c/usbc.h](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/include/zephyr/usb_c/usbc.h)、[subsys/usb/usb_c/Kconfig](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/subsys/usb/usb_c/Kconfig)、[samples/subsys/usb_c/sink/src/main.c](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/subsys/usb_c/sink/src/main.c)、[samples/subsys/usb_c/source/src/main.c](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/subsys/usb_c/source/src/main.c)、[samples/subsys/usb_c/drp/src/main.c](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/subsys/usb_c/drp/src/main.c)。

本仓库的[对应源码](../../../include/zephyr/usb_c/usbc.h)可用于跟踪，版本可能与网页不同；本批仅翻译和核对文档，没有执行固件构建、模拟运行或烧录。

<a id="usb-c-device-stack"></a>
<a id="usbc-api"></a>
<a id="configuration-options"></a>
<a id="implementing-a-sink-type-c-and-power-delivery-usb-c-device"></a>
<a id="implementing-a-source-type-c-and-power-delivery-usb-c-device"></a>
<a id="implementing-a-dual-role-power-drp-usb-c-device"></a>
<a id="api-reference"></a>
<a id="sink-callback-reference"></a>
<a id="source-callback-reference"></a>

<!-- reading-navigation:start -->

**主线阅读**

[上一篇：USBIP协议支持](P006_USBIP协议支持.md) · [本模块主线目录](../reading/usb.md) · [全部主线](../reading/README.md) · [下一篇：旧版USB设备支持](P008_旧版USB设备支持.md)

<details>
<summary>原册编号导航（含扩展参考）</summary>

[上一章](P006_USBIP协议支持.md) · [返回大纲](大纲.md) · [下一章](P008_旧版USB设备支持.md)

</details>

<!-- reading-navigation:end -->
