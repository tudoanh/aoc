### A Pluto.jl notebook ###
# v0.17.2

using Markdown
using InteractiveUtils

# ╔═╡ 4f4c8f0d-cd6e-42b1-861a-0043316f1446
md"## Day 1

[https://adventofcode.com/2021/day/1](https://adventofcode.com/2021/day/1)
"

# ╔═╡ 2c90dc2a-5260-11ec-121c-8503260899f1
input = parse.(Int64, readlines("./inputs/day_1.txt"))

# ╔═╡ 04513ffc-12c4-4157-ac7d-54436bbb0567
# Part 1

# ╔═╡ 8bd18e89-f43d-4a02-b156-02b12d9ebc29
function count_increase(input)
	len = length(input) - 1
	sum(
		(circshift(input, -1) .- input .> 0)[1:len]
	)
end

# ╔═╡ 08ae03a2-05ab-481a-8b45-b434f3a66917
count_increase(input)

# ╔═╡ e5fbca45-5a4a-4df4-9eaf-0a1942cf6d7f
# Part 2

# ╔═╡ fdec15a5-51bd-442e-b623-45b84c248a94
function sliding_window(input, depth=2)
	res = input[:]
	for i in 1:depth
		res = res .+ circshift(input, -i)
	end
	res[1:(length(res) - depth)]
end

# ╔═╡ 06eb794c-6e83-4725-8a2f-ec6cffbe8400
count_increase(sliding_window(input))

# ╔═╡ Cell order:
# ╟─4f4c8f0d-cd6e-42b1-861a-0043316f1446
# ╠═2c90dc2a-5260-11ec-121c-8503260899f1
# ╠═04513ffc-12c4-4157-ac7d-54436bbb0567
# ╠═8bd18e89-f43d-4a02-b156-02b12d9ebc29
# ╠═08ae03a2-05ab-481a-8b45-b434f3a66917
# ╠═e5fbca45-5a4a-4df4-9eaf-0a1942cf6d7f
# ╠═fdec15a5-51bd-442e-b623-45b84c248a94
# ╠═06eb794c-6e83-4725-8a2f-ec6cffbe8400
