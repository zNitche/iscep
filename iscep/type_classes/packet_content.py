from dataclasses import dataclass


@dataclass
class PacketContent:
    auth_token: str | None = None
    command: str | None = None
    args: dict[str, any] | None = None
    error: str | None = None
    response: object | None = None

    def dump(self) -> dict[str, any]:
        res = {}

        for key in self.__dict__:
            val = getattr(self, key)

            if val is not None:
                res[key] = val

        return res

    def __getattr__(self, item):
        return self.__dict__.get(item)

    def __str__(self):
        auth_token = f'{self.auth_token[:5]}...' if self.auth_token is not None else None

        attr = self.__dict__.copy()
        attr["auth_token"] = auth_token

        return f"{attr}"
