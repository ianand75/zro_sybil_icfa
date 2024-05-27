import axios from "axios";
import { delay, persistRecords, readRecords } from "mini-task-clirunner";

const apikey = "9c693aca-dd40-4988-bca3-f776e4c640d6";

const queryTx = async (tr) => {
  let page = 1;
  let retry = 1;
  let result = [];

  do {
    try {
      const url = `https://www.oklink.com/api/v5/explorer/transaction/internal-transaction-detail?chainShortName=OKTC&&page=${page}&limit=1000&txId=${tr.Txhash}`;

      await delay(1000);

      const res = await axios.get(url, {
        headers: {
          "Ok-Access-Key": apikey,
        },
      });

      const data = res.data.data[0];

      const { totalPage, internalTransactionDetails } = data;
      // console.log(data, internalTransactionDetails);

      console.log(totalPage, page);

      const rs = internalTransactionDetails.map((i) => ({
        tx: tr.Txhash,
        from: tr.from,
        to: i.to,
        value: i.amount,
      }));

      // console.log(rs);

      result = result.concat(rs);

      if (isNaN(parseInt(totalPage)) || page >= parseInt(totalPage)) break;

      page++;
    } catch (error) {
      console.log(error);
      console.log("retry");
      retry++;
      if (retry >= 3) break;
    }
  } while (true);

  return result;
};

(async () => {
  console.log(process.argv);

  const input = process.argv[2];
  const output = process.argv[3];

  const trans = readRecords(input);

  // console.log(trans);
  let result = [];
  let n = 0;
  for (const tr of trans) {
    console.log(n++, tr.value);

    const value = parseFloat(tr.value);
    if (value > 5) {
      console.log("query ", n, tr.Txhash);

      const one = await queryTx(tr);
      if (one && one.length > 0) result = result.concat(one);
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
