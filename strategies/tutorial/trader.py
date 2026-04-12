from datamodel import OrderDepth, UserId, TradingState, Order
from typing import List
import jsonpickle
import numpy as np

EMERALD_FAIR = 10000
EMERALD_EDGE = 2
POSITION_LIMIT = 80

TOMATO_WINDOW = 200
TOMATO_THRESHOLD = 4.0
TOMATO_ORDER_SIZE = 10

class Trader:

    def run(self, state: TradingState):
        result = {}
        conversions = 0

        # load price history from previous iteration
        if state.traderData and state.traderData != "":
            saved = jsonpickle.decode(state.traderData)
        else:
            saved = {"tomato_prices": []}

        tomato_prices = saved["tomato_prices"]

        for product in state.order_depths:
            orders: List[Order] = []
            position = state.position.get(product, 0)
            buy_capacity  = POSITION_LIMIT - position
            sell_capacity = POSITION_LIMIT + position

            # ── EMERALDS: market making ──────────────────────
            if product == "EMERALDS":
                if buy_capacity > 0:
                    orders.append(Order(product, EMERALD_FAIR - EMERALD_EDGE, buy_capacity))
                if sell_capacity > 0:
                    orders.append(Order(product, EMERALD_FAIR + EMERALD_EDGE, -sell_capacity))

            # ── TOMATOES: mean reversion ──────────────────────
            elif product == "TOMATOES":
                order_depth = state.order_depths[product]

                # get mid price from best bid and ask
                if order_depth.buy_orders and order_depth.sell_orders:
                    best_bid = max(order_depth.buy_orders.keys())
                    best_ask = min(order_depth.sell_orders.keys())
                    mid = (best_bid + best_ask) / 2

                    # add to price history
                    tomato_prices.append(mid)

                    # only trade once we have enough history
                    if len(tomato_prices) >= TOMATO_WINDOW:
                        rolling_mean = np.mean(tomato_prices[-TOMATO_WINDOW:])
                        deviation = mid - rolling_mean

                        # price too low — buy expecting reversion up
                        if deviation < -TOMATO_THRESHOLD and buy_capacity > 0:
                            size = min(TOMATO_ORDER_SIZE, buy_capacity)
                            orders.append(Order(product, best_ask, size))

                        # price too high — sell expecting reversion down
                        elif deviation > TOMATO_THRESHOLD and sell_capacity > 0:
                            size = min(TOMATO_ORDER_SIZE, sell_capacity)
                            orders.append(Order(product, best_bid, -size))

            result[product] = orders

        # save price history for next iteration
        # keep only last 200 prices to stay under 50k character limit
        saved["tomato_prices"] = tomato_prices[-TOMATO_WINDOW:]
        traderData = jsonpickle.encode(saved)

        return result, conversions, traderData