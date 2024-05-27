import axios from "axios";
import { delay, persistRecords, readRecords } from "mini-task-clirunner";

const urls = {
  op: `https://api-optimistic.etherscan.io/api?module=account&action=txlistinternal&apikey=Y73BTMEK5331XBN3P6S44XVHBD7HANT9P2&txhash=`,
  arb: `https://api.arbiscan.io/api?module=account&action=txlistinternal&apikey=5XPH7331JX8T3H4412QWCC5YMNM3N88FRF&txhash=`,
  polygon: `https://api.polygonscan.com/api?module=account&action=txlistinternal&apikey=D7VCGJA2IDPQ151KX56TE9G6KVECBIH22X&txhash=`,
  celo: `https://api.celoscan.io/api?module=account&action=txlistinternal&apikey=S5ZJ6CNE15JZ2DDFMP4MXQAVWQXUBMNBKP&txhash=`,
  bsc: `https://api.bscscan.com/api?module=account&action=txlistinternal&apikey=J7G5RYEQZBII4RQ6EK3ABM1BKJF98KCYH2&txhash=`,
  mr: `https://api-moonriver.moonscan.io/api?module=account&action=txlistinternal&apikey=8Z69DJX77VCEFAN684WWYP4K6FNHT76HSV&txhash=`,
  gnosis: `https://api.gnosisscan.io/api?module=account&action=txlistinternal&apikey=KAA8TXU7DIWN9B9GVX8YZHDR6FS7W4PI7G&txhash=`,
};

const fundThresholds = {
  op: 0.5,
  arb: 0.5,
  polygon: 100,
  celo: 5,
  bsc: 5,
  mr: 10,
  gnosis: 100,
};

(async () => {
  console.log(process.argv);

  const input = process.argv[2];
  const output = process.argv[3];
  const network = process.argv[4];

  if (!network) throw new Error("");

  const url = urls[network];
  const thresold = fundThresholds[network];

  const trans = readRecords(input);

  console.log(trans);
  let result = [];
  for (const tr of trans) {
    console.log(tr.Value_IN);

    const value = parseFloat(tr.Value_IN);
    if (value > thresold) {
      try {
        const res = await axios.get(url + tr.Txhash);

        const internalTrans = res.data.result;

        const rs = internalTrans.map((i) => ({ tx: tr.Txhash, from: tr.From, to: i.to, value: i.value }));

        result = result.concat(rs);
      } catch (error) {
        console.log(error);
      }

      await delay(1000);
    }

    //
  }

  const headers = [
    { id: "tx", title: "tx" },
    { id: "from", title: "from" },
    { id: "to", title: "to" },
    { id: "value", title: "value" },
  ];
  await persistRecords(output, headers, result);
})();
