import { Inter } from "next/font/google";
import styles from "./page.module.css";

const inter = Inter({ subsets: ["latin"] });

export default function Home() {
  return (
    <main className={styles.main}>
      <div className={styles.description}>
        <p>On Air Device Admin Portal</p>
      </div>

      <div className={styles.center}>
        <h2 className={inter.className}>Welcome to On Air Device</h2>
      </div>

      <div className={styles.grid}>
        <div className={styles.card}>
          <h2 className={inter.className}>
            <button>Light Switch</button>
          </h2>
          <p className={inter.className}>Turn on and off the light</p>
        </div>
      </div>
    </main>
  );
}
