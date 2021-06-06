-- phpMyAdmin SQL Dump
-- version 5.0.2
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Waktu pembuatan: 06 Jun 2021 pada 15.02
-- Versi server: 10.4.11-MariaDB
-- Versi PHP: 7.4.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `perusahaan`
--

-- --------------------------------------------------------

--
-- Struktur dari tabel `barang`
--

CREATE TABLE `barang` (
  `idBarang` int(11) NOT NULL,
  `namaBarang` varchar(100) NOT NULL,
  `stok` int(11) NOT NULL,
  `hargaBarang` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data untuk tabel `barang`
--

INSERT INTO `barang` (`idBarang`, `namaBarang`, `stok`, `hargaBarang`) VALUES
(1, 'sabun', 23, 8000),
(2, 'kecap', 15, 9000),
(4, 'roti', 15, 2500),
(5, 'mie goreng', 10, 1500),
(6, 'sosis', 23, 3000),
(8, 'sarung', 5, 50000),
(9, 'saos', 10, 8500),
(10, 'garam', 5, 2500),
(12, 'gula', 13, 5500),
(14, 'teh', 20, 1500),
(15, 'susu', 5, 5500);

-- --------------------------------------------------------

--
-- Struktur dari tabel `login`
--

CREATE TABLE `login` (
  `idUser` int(10) NOT NULL,
  `username` varchar(50) NOT NULL,
  `password` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data untuk tabel `login`
--

INSERT INTO `login` (`idUser`, `username`, `password`) VALUES
(1, 'syaifqr', 'syaif123'),
(2, 'uliaaa', 'ulia26'),
(3, 'ichwan', 'ichwan45'),
(4, 'alpin', 'alpin123'),
(5, 'iqbal', 'iqbal123');

-- --------------------------------------------------------

--
-- Struktur dari tabel `transaksi`
--

CREATE TABLE `transaksi` (
  `idOrder` int(11) NOT NULL,
  `idBarang` int(11) NOT NULL,
  `jumlah` int(11) NOT NULL,
  `jenis_transaksi` varchar(10) NOT NULL,
  `time` datetime NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data untuk tabel `transaksi`
--

INSERT INTO `transaksi` (`idOrder`, `idBarang`, `jumlah`, `jenis_transaksi`, `time`) VALUES
(1, 1, 3, 'masuk', '2021-01-01 22:11:20'),
(2, 5, 10, 'keluar', '2021-01-01 23:59:21'),
(3, 5, 5, 'masuk', '2021-01-02 00:03:10'),
(4, 1, 1, 'masuk', '2021-01-02 09:14:38'),
(5, 1, 7, 'masuk', '2021-01-11 14:55:17'),
(6, 2, 1, 'masuk', '2021-06-06 00:09:29'),
(8, 10, 10, 'keluar', '2021-06-06 01:13:32'),
(9, 1, 10, 'keluar', '2021-06-06 01:14:27'),
(10, 2, 5, 'keluar', '2021-06-06 19:53:24');

--
-- Indexes for dumped tables
--

--
-- Indeks untuk tabel `barang`
--
ALTER TABLE `barang`
  ADD PRIMARY KEY (`idBarang`);

--
-- Indeks untuk tabel `login`
--
ALTER TABLE `login`
  ADD PRIMARY KEY (`idUser`);

--
-- Indeks untuk tabel `transaksi`
--
ALTER TABLE `transaksi`
  ADD PRIMARY KEY (`idOrder`),
  ADD KEY `idBarang` (`idBarang`);

--
-- AUTO_INCREMENT untuk tabel yang dibuang
--

--
-- AUTO_INCREMENT untuk tabel `barang`
--
ALTER TABLE `barang`
  MODIFY `idBarang` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=16;

--
-- AUTO_INCREMENT untuk tabel `login`
--
ALTER TABLE `login`
  MODIFY `idUser` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT untuk tabel `transaksi`
--
ALTER TABLE `transaksi`
  MODIFY `idOrder` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- Ketidakleluasaan untuk tabel pelimpahan (Dumped Tables)
--

--
-- Ketidakleluasaan untuk tabel `transaksi`
--
ALTER TABLE `transaksi`
  ADD CONSTRAINT `transaksi_ibfk_1` FOREIGN KEY (`idBarang`) REFERENCES `barang` (`idBarang`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
